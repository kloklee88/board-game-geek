import random

def get_rankings():
  ranking_display = ''
  with open('rankings.txt') as message_text:
    for line in message_text:
      split_line = line.split(';')
      username = split_line[0]
      rankings = split_line[1]
      ranking_display += '**' + username + '**\n' + rankings
  print(ranking_display)
  return ranking_display

def get_collection():
  collection = ''
  with open('collection.txt') as message_text:
    for line in message_text:
      game = line.split('|')[0]
      collection += game + '\n'
  return collection

def lookup_game(game_name):
  game_detail = ''
  print(game_name)
  with open('collection.txt') as message_text:
    for line in message_text:
      game = line.split('|')[0].strip()
      if game_name.lower() in game.lower():
        game_detail += line.split('|')[0] + " | Max Players: " + line.split('|')[1] + " | " + line.split('|')[2] + "\n"
  if game_detail == '':
    return 'Game not Found'
  return game_detail

def random_game(player_count):
  collection = []
  with open('collection.txt') as message_text:
    for line in message_text:
      clean_line = line.replace("\n", " ").strip()
      game = clean_line.split('|')[0]
      max_player = clean_line.split('|')[1].strip()
      if int(max_player) > int(player_count):
        collection.append(game)
  print(collection)
  return random.choice(collection)

def get_help():
  f = open('help.txt')
  help = f.readlines()
  return ''.join(help)
