def get_rankings():
  with open('rankings.txt') as message_text:
    for line in message_text:
      game_ranking = line.replace("\n", " ").strip()
      username = game_ranking.split(';')[0]
      if username in user.name:
        rankings = game_ranking.split(';')[1]
  print(rankings)
  return rankings

def get_collection():
  f = open('collection.txt')
  help = f.readlines()
  return ''.join(help)

def get_help():
  f = open('help.txt')
  help = f.readlines()
  return ''.join(help)