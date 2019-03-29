import json

with open('gameData.json') as json_data:
	jsonData = json.load(json_data)
for day in jsonData:
	for game in day['data']:
		if game['homeScore']>game['awayScore']:
			print("H " + game['homeTeam'] + " " + str(game['homeScore']) + " - " + game['awayTeam'] + " " + str(game['awayScore']))
		else:
			print("A " + game['awayTeam'] + " " + str(game['awayScore']) + " - " + game['homeTeam'] + " " + str(game['homeScore']))

		