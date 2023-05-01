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
  with open('collection.txt') as message_text:
    for line in message_text:
      collection_file = line.replace("\n", " ").strip()
      game = collection_file.split('|')[0]
      if game in game_name:
        game_detail = collection_file.split('|')[2]
  return game_detail


def get_help():
  f = open('help.txt')
  help = f.readlines()
  return ''.join(help)
