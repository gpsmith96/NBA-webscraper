import json

with open('gameData.json') as json_data:
	jsonData = json.load(json_data)
for day in jsonData:
	for game in day['data']:
		if int(game['homeScore'])>int(game['awayScore']):
			print(game['homeTeam'] + " " + game['homeScore'] + " - " + game['awayTeam'] + " " + game['awayScore'])
		else:
			print(game['awayTeam'] + " " + game['awayScore'] + " - " + game['homeTeam'] + " " + game['homeScore'])

		