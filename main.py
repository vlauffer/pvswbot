
import requests
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
client = discord.Client()

# gets all messages within a given time frame (determined by time_delta), 
# creates object that contains message information, and prompts send_inserted_messages()
async def get_all_messages():

  messages_to_send =[]
  time_to_get_messages = datetime.datetime.utcnow()- datetime.timedelta(seconds=time_delta)

  all_channels_raw = client.get_all_channels()
  all_channels = tuple(all_channels_raw)

  # for every channel in the Discord guild, test to see if the channel is a Text Channel. 
  # if the channel is a Text Channel, get messages within a given time interval from now, and add them
  # to the messages_to_send array
  for channel in all_channels:
    if type(channel).__name__=='TextChannel':
      try: 
        channel_history = await channel.history(limit=None, after=time_to_get_messages).flatten()
        for message in channel_history:
          
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
      except:
        continue
  if len(messages_to_send)>0:
    send_inserted_messages(messages_to_send)

# sends array of message objects to the backend for insertion
def send_inserted_messages(messages):
  
  data = {'messages': messages}
  try:
    response = requests.post(active_url+insert_url, timeout=5, json = data)
    print(response)

  except requests.exceptions.RequestException as e:
    print (e)

# Called whenever a message is edited. creates message object and invokes send_edited_message to send message to the backend
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
  
# Sends an edited message to the backend
def send_edited_message(message):  
  data = {'message': message}
  try:
    response = requests.post(active_url+edit_url, timeout=5, json = data)
    print(response)

  except requests.exceptions.RequestException as e:
    print (e)

#called every time a message is deleted, and invokes send_deleted_message
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

# called whenever a reaction is added, regardless of its cached value.
# invokes Send a reaction to the backend
@client.event
async def on_raw_reaction_add(payload):
  send_added_reaction(payload)

# future functionality: inserting reactions into db
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

async def spam(all_channels ):
  counter = 0
  for channel in all_channels:
    if type(channel).__name__=='TextChannel':
      try: 
        counter = counter+1
        await channel.send(lorem[counter%5])
        await channel.send(lorem[counter%5])
        await channel.send(lorem[counter%5])
        await channel.send(lorem[counter%5])
        await channel.send(lorem[counter%5])
        await channel.send(lorem[counter%5])

      except:
        continue
  return

# Event that helps us track if the bot is online (will be removed in a production environment)
@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith("$b"):
    #discord.utils.find() or just use str.find(message.content,"🥞")
    varia = message.guild
    await spam(varia.channels)

  if message.content.startswith("🥞"):
    #discord.utils.find() or just use str.find(message.content,"🥞")
    await message.channel.send("+10 pancake points")
    
  if message.content.startswith("🧇"):
    await message.channel.send("+10 waffle points") 


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
