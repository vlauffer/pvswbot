
from concurrent.futures import thread
import requests
import discord
from discord.ext import tasks, commands
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

lorem = ["Enim 📰🍢🍩🕝🍕🌄🐸🕙🎱🎳📳💹 proin 💝🔨🎺📈🗽🍭👰 in 🔹🔞🔴👒🕔🔂🕛 nulla enim 🌕🕠📏🔺 magna pharetra nunc, 🍑📠🔵🍯🍀🍛 sit condimentum non risus 👇🕕🏆🏫🐺 🎻🏯👸🎧🔥 orci nunc 👾🍎🌉🎶🔦 libero venenatis, augue aenean ultrices 🎋🏰🐚🎹🐋💆🌍📪🎭🔆🎮💪👀🎅 🍳🔲🍚🎨🌵🎑👟🔈🎀👔🕝🎁 👼🐼💐🐴 🐈💽👓📬📰🎳 volutpat facilisis turpis 👈📖💬📫🔨 convallis quam 👛👇📬💑🍗🌠💉💒 🔗📓🍭🐼👱📫🍐🌕 ut 👋🎴🐕🗻 accumsan 🍢🐠🐥📂🔵🎇🔱🎺🌆 🎾🎴📳🍓🕧🐓🐨🏈🔄🔄 in convallis 🐹🔆👠🐩📘📲🎒🐟📷🐢🐒💓🎀 proin viverra sit vulputate 🍄🕢🐰💃🎈 interdum 👜📮🕥👑🍄🐐🍀🍸🕚 🕖🔆🎈🌐🐜 👢👹🍶💿🎾👏💾🏃🐌🔷 enim aliquet 🍨🍹🕙🔈🎶🐸 tristique 🍩👨🐵👢🌑 ac, elementum, curabitur imperdiet 🍥💼🗽🏭🌍 nunc, scelerisque facilisis vestibulum 📇🎍📒🐖🕗🕕📓 arcu 📟🔪👴📗 📯💸👱🐉🍚 🔥🍍📼👕👍🕝🔂💶 nunc, justo nunc at 📓🌱🎍👝🎹🔊🔹👐 🌕📫🏨🎁🕚🐖🔓🐇🎷🌷🔰🐜📣🎋 donec 🔈💜🍗🔱🎻🍏🌏🌓🍆💃🍢🏯🐐 natoque fermentum 🍱🔥🌰🏬📳🍳 non in. 🏤🏩🎪👟🍻👐🎧🔲🔟🎺📊 💃🗽📓🔴 nunc et non",
"dictum dui, malesuada magna 🐲🏣🔰👻🐷🌱👢 pellentesque duis 💐💔📠👸🕤 📲🐕🏮📹🏭🐦🏮📏🍆🏠🔌💽🏪🎧 sed 🌽🏭🌺🎷 🐣🌵💅👛🔟🔨 🔋🐺💦🐊🎺 🍚📯🎈📃 quis 💤🐰🐠📬 tempor ullamcorper viverra massa 🕑📆🌀👎🔑💒🐒🍄🎧🍙🍪🕁🍰👐 nulla semper 🍏🎺🌟🐏 👤🍅🔲👄🎧📣🌵🍂 consectetur in 💫🍜🐕🌰 curabitur 📓🌏🌖📩🔫👚🌵🔣🔤🏬🍎🌽👅🎿 🍦📄📥📕🔩🏦🐚🎷 🎦💌🔭🕤🐢🐏🍀🕘🏂👌📺🔡🔼 🍈🕁🐖🏣🕞🐒 🏥🔇💃💬🍦👻 🐟🏤🌾👩📋🕤🎢💉📠🗾 🗻🔯💠🐝🌀🎣 posuere 💆🏤👢🔯🐌💸 lobortis 🔁🎣🌏🎱💈💔 📠👑🎱🔙 proin 📝🔨🍬🔂🍍🔭🔮🔻🔚🌠🎤🍶🔇. Semper adipiscing risus 🔷🔜🍄🔟🔂🕜🌁🍔🌔🐺🐼🔌 nibh et 🍑👬🍵",
"👻📠🐢🌲🎪🏊🔲🕘🍼🌹🐡💱🍆 vitae 💼🎎🎮🐛 👦🕀👓🐣🌇📥🐰🎂👦🔀🏰🔴 🍪💒🏉📤🏦📔🔼💬🔤🎹👳 🔜🌕🏦🔴 🐁🍥🏇🏫 gravida enim pellentesque eget maecenas bibendum arcu 🐚🔥🍫🔻💼💦💼🐍👙🎑 ullamcorper 🐗🔥👲🕕🐼💖 tortor sed in 🐒📖🍷👨 lacus, pharetra blandit 🕗🏊📱🐯👏💄👄 elit lectus 🍳👘🔓🌝💓🍘💺🎄🏠🔡🔔🎰🔛🔬 💅📐👥💜💇🐎🕦 🍌🌆🌵📯👋💎🕔🍒 🗽🔛🐜🐽🌁💫💍 magna auctor 📍🐖👉🎭📯📝🌾📁🔀🔥🔍🔸🐊🔤💐 🔜🔙📜🍡💊🌏 vulputate proin id vestibulum, vel natoque 🔞🎨🍩🎃👖📞🔲 🕜🍶📰🐒🍁🌉🕁 💖👰💭🔌🍌💷💯👺🍫🍙🌰🎡🐋🐧💭🏡🌘🍥 🐩🔸🔆🐪💢🎌🍎🌼🔙🔘🍸🔥 eget pulvinar cursus 💸📮🎲📳 vitae 📑",
"📊📬💺🐛🐇 🍏🌌🔰👜 varius lobortis 💞🕐📈📝 sed amet, nisl 🍪🔨📟🔍💅📢👖🎌 laoreet mi 📨💗👒🐢👤📈🏮🏫📝🗾🔄🌺🐙🍗📦📆🌑📟🍳 🔼🍧🔑🗻👞🍂📻👄🏣👫🐴🐷🌺💸🕣 tristique 🕗👷🐭👊🎷🎍 in 🎎💊📇📋💪🐑 sed vitae 🕚📻👮🐊📭📜 lectus 💇📁🏫🌔💝🌿🏩👺 dapibus hendrerit 🎃🐏💀👒🕙🔞🌖 💲🐸👛🔘🕗 in 🐙🔐🕀🐵👱🍼 quis quisque ullamcorper sociis. Amet, 🐁🎬📫🌲💚🌘🍶📣👺🔌 tempor 👬🔲💱🐸🌚🍤 faucibus 🎵🐻🎓🎅🗾💑👣👆🌖🌎 adipiscing purus 🔍🐓💹👱👌🍜📓📯🍳🐡👳🎸🎱🔘 auctor sed 📫📁🐏",
"🎠🐱🎵💍💸🎶🔩👔🔔🔷🍑 🎬🍩🌟👘📝🐚📢🍦🎂📫 🎲🎃🌘📁💿🏧👮🍮📕💮🎻🌹💬🔵🔀 🎇💽🕜🍔🍘👛 🎾🎃🎃🍛🎼🌅🏤💫🐖🌏🍦🕜🌿🍱🗽🍖 🌲🌲🌸🌳💶🔵🔕 sollicitudin vivamus 🏢🐃🐥🍷📆🕛🌼🐸🔀🌽🍞👤💫🍼 ipsum tempus 🔙🔭💪🎨🐎🍷🍼🐚🎑🐮🔱🌹🎨 suscipit nisi 💅🌲🐕🐮🎫👸🔆🎿 consectetur id vestibulum nunc adipiscing egestas consectetur convallis id lacus est et."
]

# sets request url and token, which is determined by the existance of the secrets file.
# if no secrets file is found, sets active_url to production url and token to the discord bot token found in heroku.
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
 

# the amount of seconds between each call of get_all_messages. This wait time is set in looper()
time_delta = 10

# creation of the discord client
client = discord.Client(intents=discord.Intents.all())

# gets all messages within a given time frame (determined by time_delta), 
# creates object that contains message information, and prompts send_inserted_messages()
async def get_all_messages():

  messages_to_send =[]

  #  messages will be fetched if they are sent after time_to_get_messages.
  time_to_get_messages = datetime.datetime.utcnow()- datetime.timedelta(seconds=10) -  datetime.timedelta(hours=4)

  # get all channels
  all_channels_raw = client.get_all_channels()
  all_channels = tuple(all_channels_raw)

  # get all guilds
  guild = client.guilds[0]
  threads = guild.threads

  #for each thread, get all messages with their reactions and add them to messages_to_send
  for thread in threads:
    try: 
      thread_messages = await get_thread_messages(thread, time_to_get_messages)
      messages_to_send += thread_messages
    except:
      continue

  # for every channel in the Discord guild, test to see if the channel is a Text Channel. 
  # if the channel is a Text Channel, get messages within a given time interval from now, and add them
  # to the messages_to_send array
  for channel in all_channels:
    if type(channel).__name__=='TextChannel':
      try: 
        channel_messages = await get_channel_messages(channel, time_to_get_messages)
        messages_to_send += channel_messages
      except:
        continue

  # if there are any messages, send them to the backend
  if len(messages_to_send)>0:
    send_inserted_messages(messages_to_send)


# extract all channel messages sent after a given time, as well as each messages reactions, and return them in an array
async def get_channel_messages(channel, time_to_get_messages):
  messages_to_send = []
  
  # iterate through all messages, which are fetched after the time in time_to_get_messages
  async for message in channel.history(limit=500, after=time_to_get_messages):
          
    #get all reactions in the message
    reactions = []
    for reaction in message.reactions:
      reaction_struct = {
        "user_id": reaction.message.author.id,
        "channel_id": reaction.message.channel.id,
        "message_id": reaction.message.id,
        "content": reaction.emoji,
        "created_at": reaction.message.created_at.strftime("%Y-%m-%d %H:%M:%S")
      }
      reactions.append(reaction_struct)
    #create message structure
    message_struct = {
      "username": message.author.display_name +"#"+ message.author.discriminator,
      "user_id": message.author.id,
      "channel_id": message.channel.id,
      "message_id": message.id,
      "content": message.content,
      "reactions": reactions,
      "created_at": message.created_at.strftime("%Y-%m-%d %H:%M:%S")
    }     
    messages_to_send.append(message_struct)
  
  return messages_to_send

#extract all messages and reactions from threads sent after a given time, and return them in an array
async def get_thread_messages(thread, time_to_get_messages):
  messages_to_send = []
  print(time_to_get_messages)
  new_messages = [message async for message in thread.history(limit=100)]
  async for message in thread.history(limit=None, after=time_to_get_messages):

    #get all reactions in the message
    reactions = []
    for reaction in message.reactions:
      reaction_struct = {
        "user_id": reaction.message.author.id,
        "channel_id": reaction.message.channel.id,
        "message_id": reaction.message.id,
        "content": reaction.emoji,
        "created_at": reaction.message.created_at.strftime("%Y-%m-%d %H:%M:%S")
      }
      reactions.append(reaction_struct)

    message_struct = {
      "username": message.author.display_name +"#"+ message.author.discriminator,
      "user_id": message.author.id,
      "channel_id": message.channel.id,
      "message_id": message.id,
      "content": message.content,
      "reactions": reactions,
      "created_at": message.created_at.strftime("%Y-%m-%d %H:%M:%S")
    }     
    messages_to_send.append(message_struct)

  return messages_to_send


# sends array of message objects to the backend for insertion
def send_inserted_messages(messages):
  
  data = {'messages': messages}
  try:
    response = requests.post(active_url+insert_url, timeout=5, json = data)
    print(response)

  except requests.exceptions.RequestException as e:
    print (e)

# called whenever a message is edited. creates message object and invokes send_edited_message to send message to the backend
@client.event
async def on_raw_message_edit(payload):
  message = {
    "username": payload.data['author']['username'],
    "user_id": payload.data['author']['id'],
    "content": payload.data['content'],
    "channel_id": payload.channel_id,
    "message_id": payload.message_id,
    "created_at":  datetime.datetime.fromisoformat(payload.data['timestamp']).strftime("%Y-%m-%d %H:%M:%S")
  }
  send_edited_message(message)
  
# sends an edited message to the backend
def send_edited_message(message):  
  data = {'message': message}
  try:
    response = requests.post(active_url+edit_url, timeout=5, json = data)
    print(response)

  except requests.exceptions.RequestException as e:
    print (e)

# called every time a message is deleted, and invokes send_deleted_message
@client.event
async def on_raw_message_delete(payload):
  send_deleted_message(payload.message_id)

#sends a message_id to the backend for deletion
def send_deleted_message(message_id):
  data = {'message_id': message_id}
  try:
    response = requests.post(active_url+delete_url, timeout=5, json = data)
    print(response)

  except requests.exceptions.RequestException as e:
    print (e)

# called whenever a reaction is added, regardless of its cached value, send it along to send_added_reaction()
@client.event
async def on_raw_reaction_add(payload):
  send_added_reaction(payload)

# sends reactions into db
def send_added_reaction(payload):
  reaction_struct = {
    "user_id": payload.user_id,
    "channel_id": payload.channel_id,
    "message_id": payload.message_id,
    "content": payload.emoji.name,
    "created_at": datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
  }

  data = {'reaction': reaction_struct}
  try:
    response = requests.post(active_url+ add_reaction_url, timeout=5, json = data)
    print(response)

  except requests.exceptions.RequestException as e:
    print (e)
  print(payload.emoji.name)


# called whenever a reaction is added, regardless of its cached value.
@client.event
async def on_raw_reaction_remove(payload):
  send_removed_reaction(payload)

# send a reaction to the backend for deletion
def send_removed_reaction(payload):
  reaction_struct = {
    "user_id": payload.user_id,
    "message_id": payload.message_id,
    "content": payload.emoji.name
  }

  data = {'reaction': reaction_struct}
  try:
    response = requests.post(active_url+ remove_reaction_url, timeout=5, json = data)
    print(response)

  except requests.exceptions.RequestException as e:
    print (e)
  print(payload.emoji.name)


#checks if character is a component of a flag emoji
def is_flag_emoji(c):
  return "\U0001F1E6\U0001F1E8" <= c <= "\U0001F1FF\U0001F1FC" or c in ["\U0001F3F4\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f", "\U0001F3F4\U000e0067\U000e0062\U000e0073\U000e0063\U000e0074\U000e007f", "\U0001F3F4\U000e0067\U000e0062\U000e0077\U000e006c\U000e0073\U000e007f"]

# checks to see if there is an emoji in the text
def text_has_emoji(text):
  for character in text:
    flagcheck = is_flag_emoji(character)
    if character in emoji.UNICODE_EMOJI['en'] or flagcheck:
      return True
  return False


# Event that helps us track if the bot is online 
@client.event
async def on_message(message):
  if message.author == client.user:
    return

  # whenever there is a message that starts with $🥞 or $🧇, send author a message
  if message.content.startswith("$🥞"):
    await message.author.send("PANCAKE GANG!!!")
    
  if message.content.startswith("$🧇"):
    await message.author.send("WAFFLE GANG!!!") 


# initializes the bot and calls the looper function in order to start fetching messages at a given interval
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
  await looper.start()

# loops the get_all_messages() function at given interval determined by time_delta (seconds)
@tasks.loop(seconds=time_delta)
async def looper():
  await get_all_messages()
  print("🥞🥞🥞🥞🥞")
 

#starts the bot
client.run(token)
