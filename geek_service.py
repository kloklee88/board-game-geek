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
  game_detail = 'Game not found'
  with open('collection.txt') as message_text:
    for line in message_text:
      game = line.split('|')[0].strip()
      if game in game_name.lower():
        game_detail = line.split('|')[1].strip()
  return game_detail

def random_game(player_count):
  collection = []
  with open('collection.txt') as message_text:
    for line in message_text:
      game = line.replace("\n", " ").strip().split('|')[0]
      #add logic to filter out games by max players and add to collection.txt
      collection.append(game)
  return random.choice(collection)


def get_help():
  f = open('help.txt')
  help = f.readlines()
  return ''.join(help)
