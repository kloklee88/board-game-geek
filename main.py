import discord
import os
import geek_service
from keep_alive import keep_alive

#Flask Server to keep repl.it alive
keep_alive()

intents = discord.Intents.all()
intents.members = True
intents.presences = True
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
  activity = discord.Game(name="!geek help")
  await client.change_presence(activity=activity)
  print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  #Process message commands
  full_command = message.content.strip().split(' ')

  if message.content.startswith('!geek'):
    print(full_command)
    if len(full_command) == 2:
      first_command = full_command[1]
      if first_command == 'about':
        await message.channel.send(about())
      elif first_command == 'help':
        await message.channel.send(geek_service.get_help())
      elif first_command == 'collection':
        await message.channel.send(geek_service.get_collection())
      elif first_command == 'rankings':
        await message.channel.send(geek_service.get_rankings())
    elif len(full_command) == 3:
      first_command = full_command[1]
      if first_command.startswith('lookup'):
        second_command = full_command[2]
        await message.channel.send(geek_service.lookup_game(second_command))


def about():
  return "A dedicated Discord bot for He's a Board Game Group server for everything, anything, and nothing :smile:"


client.run(os.getenv('TOKEN'))
