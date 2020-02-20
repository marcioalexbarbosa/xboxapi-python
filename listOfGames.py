from xboxapi import Client

client = Client(api_key='REPLACE WITH YOUR API KEY')
gamer = client.gamer(gamertag='REPLACE WITH YOUR GAMERTAG', xuid='REPLACE WITH YOUR XBOX PROFILE USER ID')

games = gamer.get('xboxonegames')

titles = games['titles']

for game in titles:
    print (game['name'])
