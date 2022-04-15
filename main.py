
import requests
import json
import discord
from discord.ext import tasks
import os
import emoji
import datetime


token =""
prod_url = "https://pvswbot-backend.herokuapp.com"
local_url = "http://localhost:3000"
insert_url = "/messages/add"
edit_url = "/messages/edit"
delete_url = "/messages/delete"
add_reaction_url = "/reaction/add"
remove_reaction_url = "/reaction/remove"
active_url=""

# sets request url and token, which is determined by the existance of the secrets file
try:
  from secrets import TOKEN
except:
  print("NO SECRETS FILE. ATTEMPTING TO RETRIEVE TOKEN FROM ENV")
  token= os.environ['TOKEN']
  active_url=prod_url
  
else:
  print("TOKEN FOUND IN SECRETS FILE")
  token = TOKEN
  active_url=local_url
 

# interval in which to get new messages
time_delta = 10

client = discord.Client()

# sends array of message objects to the backend for insertion
def insert_messages(messages):
  
  print("Inserting pancakes (and other emojis)")

  data = {'messages': messages}
  try:
    response = requests.post(active_url+insert_url, timeout=5, json = data)
    print(response)

  except requests.exceptions.RequestException as e:
    print (e)

# Future functionality: inserting reactions into db
def insert_reaction(payload):
  reaction_struct = {
    # "username": message.author.display_name +"#"+ message.author.discriminator,
    "user_id": payload.user_id,
    "channel_id": payload.channel_id,
    "message_id": payload.message_id,
    "content": payload.emoji.name,
    "created_at": datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
  }

  print("Inserting reactions")

  data = {'reaction': reaction_struct}
  try:
    response = requests.post(active_url+ add_reaction_url, timeout=5, json = data)
    print(response)

  except requests.exceptions.RequestException as e:
    print (e)
  print(payload.emoji.name)

#checks for flag
def is_flag_emoji(c):
  return "\U0001F1E6\U0001F1E8" <= c <= "\U0001F1FF\U0001F1FC" or c in ["\U0001F3F4\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f", "\U0001F3F4\U000e0067\U000e0062\U000e0073\U000e0063\U000e0074\U000e007f", "\U0001F3F4\U000e0067\U000e0062\U000e0077\U000e006c\U000e0073\U000e007f"]

# checks to see if there is an emoji in a string
def text_has_emoji(text):
  


  
  

  for character in text:
    flagcheck = is_flag_emoji(character)
    if character in emoji.UNICODE_EMOJI['en'] or flagcheck:
      # emojilist = 
      
      return True
  return False


# gets all messages within a given time frame (determined by time_delta), 
# creates object that contains message information, and prompts insert_messages()
async def get_all_messages():

  messages_to_send =[]
  time_to_get_messages = datetime.datetime.utcnow()- datetime.timedelta(seconds=time_delta)

  all_channels_raw = client.get_all_channels()
  all_channels = tuple(all_channels_raw)

  # for every channel in the Discord guild, test to see if the channel is a Text Channel. 
  # if the channel is a Text Channel, get messages within a given time interval from now, and add them
  # ti the messages_to_send array
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
              "created_at": message.created_at.strftime("%Y-%m-%d %H:%M:%S")
            }     
            messages_to_send.append(message_struct)
      except:
        continue
  if len(messages_to_send)>0:
    insert_messages(messages_to_send)

def remove_reaction(payload):
  reaction_struct = {
    # "username": message.author.display_name +"#"+ message.author.discriminator,
    "user_id": payload.user_id,
    "message_id": payload.message_id,
    "content": payload.emoji.name
    
  }

  print("removing reaction")

  data = {'reaction': reaction_struct}
  try:
    response = requests.post(active_url+ remove_reaction_url, timeout=5, json = data)
    print(response)

  except requests.exceptions.RequestException as e:
    print (e)
  print(payload.emoji.name)


# initializes the bot and calls the looper function in order to start fetching messages at a given interval
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
  # insert_messages("messages_to_send")
  await looper.start()

# Event that helps us track if the bot is online (will be removed in a production environment)
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

@client.event
async def on_raw_message_edit(payload):
  date = datetime.datetime.fromisoformat(payload.data['timestamp']).strftime("%Y-%m-%d %H:%M:%S")
  message = {
    "username": payload.data['author']['username'],
    "user_id": payload.data['author']['id'],
    "content": payload.data['content'],
    "channel_id": payload.channel_id,
    "message_id": payload.message_id,
    "created_at":  datetime.datetime.fromisoformat(payload.data['timestamp']).strftime("%Y-%m-%d %H:%M:%S")
  }
  edit_messages(message)
  

def edit_messages(message):  
  print("Editing pancakes (and other emojis)")
  data = {'message': message}
  try:
    response = requests.post(active_url+edit_url, timeout=5, json = data)
    print(response)

  except requests.exceptions.RequestException as e:
    print (e)


@client.event
async def on_raw_message_delete(payload):
  delete_message(payload.message_id)

def delete_message(message):
  print("delete message %d" % message)

  data = {'message': message}
  try:
    response = requests.post(active_url+delete_url, timeout=5, json = data)
    print(response)

  except requests.exceptions.RequestException as e:
    print (e)

# Testing functionality for reaction adding
@client.event
async def on_raw_reaction_add(payload):
  insert_reaction(payload)

@client.event
async def on_raw_reaction_remove(payload):
  remove_reaction(payload)




# loops a given function, in this case, get_all_messages(), at given interval determined by time_delta (seconds)
@tasks.loop(seconds=time_delta)
async def looper():
  await get_all_messages()
  print("🥞🥞🥞🥞🥞")
 
#starts the bot
client.run(token)
