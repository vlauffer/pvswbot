
import requests
import json
import discord
from discord.ext import tasks
import os
import emoji
import datetime

token =""
req_url = ""

# Sets request url and token, which is determined by the existance of the secrets file
try:
  from secrets import TOKEN
except:
  print("NO SECRETS FILE. ATTEMPTING TO RETRIEVE TOKEN FROM ENV")
  token= os.environ['TOKEN']
  req_url="https://pvswbot-backend.herokuapp.com/insertmessages"
  
else:
  print("TOKEN FOUND IN SECRETS FILE")
  token = TOKEN
  req_url="http://localhost:3000/insertmessages"

#interval in which to get new messages
time_delta = 10

client = discord.Client()

#sends array of message objects to the backend for insertion
def insert_messages(messages):
  
  print("Inserting pancakes (and other emojis)")

  data = {'messages': messages}
  try:
    response = requests.post(req_url, timeout=5, json = data)
    print(response)

  except requests.exceptions.RequestException as e:
    print (e)

# Future functionality: inserting reactions into db
async def insert_reaction(payload):
  print(payload.emoji)

#checks to see if there is an emoji in a string
def text_has_emoji(text):
  for character in text:
    if character in emoji.UNICODE_EMOJI['en']:
      return True
  return False


#gets all messages within a given time frame (determined by time_delta), 
# creates object that contains message information, and prompts insert_messages()
async def get_all_messages():

  messages_to_send =[]
  time_to_get_messages = datetime.datetime.utcnow()- datetime.timedelta(seconds=time_delta)

  all_channels_raw = client.get_all_channels()
  all_channels = tuple(all_channels_raw)
  for channel in all_channels:

    if type(channel).__name__=='TextChannel':
      
      try: 
        # channel_history = await channel.history(limit=5).flatten()
        channel_history = await channel.history(limit=None, after=time_to_get_messages).flatten()
        for message in channel_history:
          if text_has_emoji(message.content):
            message_struct = {
              "username": message.author.display_name +"#"+ message.author.discriminator,
              "user_id": message.author.id,
              "channel_id": message.channel.id,
              "message_id": message.id,
              "content": message.content,
            }     
            messages_to_send.append(message_struct)
      except:
        continue
  insert_messages(messages_to_send)

#Initializes the bot and calls the looper function
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
  # insert_messages("messages_to_send")
  await looper.start()

#Event that helps us track if the bot is online (will be removed in a production environment)
@client.event
async def on_message(message):
  if message.author == client.user:
    return
    
  print(text_has_emoji(message.content))

  if message.content.startswith("🥞"):
    #discord.utils.find() or just use str.find(message.content,"🥞")
    await message.channel.send("+2000 pancake points")
    
  if message.content.startswith("🧇"):
    await message.channel.send("+10 waffle points") 

#Testing functionality for reaction adding
@client.event
async def on_raw_reaction_add(payload):
  insert_reaction(payload)
  if payload.emoji.name=="🧇":
    print(payload.emoji)


#loops a given function, in this case, get_all_messages(), at given interval determined by time_delta in seconds
@tasks.loop(seconds=time_delta)
async def looper():
  await get_all_messages()
  print("🥞🥞🥞🥞🥞")
 
#starts the bot
client.run(token)
