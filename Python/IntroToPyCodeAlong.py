import yaml
import os

script_dir = os.path.dirname(__file__)
rel_path = 'Data\\file.yaml'
path = os.path.join(script_dir, rel_path)

f = open(path)
data = yaml.safe_load(f)
f.close()

typeOfData = type(data)

city = data['info']['city']
venue = data['info']['venue']
teams = data['info']['teams']
teamsCount = len(teams)

tossWinner = data['info']['toss']['winner']
winnerDecision = data['info']['toss']['decision']

firstBaller = data['innings'][0]['1st innings']['deliveries'][0][0.1]['bowler']
firstBatsman = data['innings'][0]['1st innings']['deliveries'][0][0.1]['batsman']

totalDelevries1stInning = len(data['innings'][0]['1st innings']['deliveries'])
totalDelevries2ndInning = len(data['innings'][1]['2nd innings']['deliveries'])

winner = data['info']['outcome']['winner']
winnerBy = data['info']['outcome']['by']

print(typeOfData,city,venue,teams,teamsCount,tossWinner,winnerDecision,sep="\n")
print(firstBaller,firstBatsman,totalDelevries1stInning,totalDelevries2ndInning,sep="\n")
print(winner,winnerBy,sep="\n")
