'''
Created on May 30, 2019

@author: WONDER
'''
import os
import yaml
from collections import Counter
 
script_dir = os.path.dirname(__file__)
rel_path = 'Data\\file.yaml'
path = os.path.join(script_dir, rel_path)
 
f = open(path)
data = yaml.safe_load(f)
f.close()

ballCount = 0
for deliveries in data['innings'][0]['1st innings']['deliveries']:
    if deliveries[list(deliveries.keys())[0]]['batsman'] == "SC Ganguly":
        ballCount += 1
print(ballCount)
 
batsman1stInnings = Counter()
for deliveries in data['innings'][0]['1st innings']['deliveries']:
    batsman1stInnings.update([deliveries[list(deliveries.keys())[0]]['batsman']])
ballCount=batsman1stInnings.get("SC Ganguly")
print(ballCount)

SC_Ganguly = data['innings'][0]['1st innings']['deliveries'][0:]
# x = {0.1: {'batsman': 'SC Ganguly', 'bowler': 'P Kumar', 'extras': {'legbyes': 1}, 'non_striker': 'BB McCullum', 'runs': {'batsman': 0, 'extras': 1, 'total': 1}}}
x = "'batsman': 'SC Ganguly'"
print(str(SC_Ganguly).count(x))
print(SC_Ganguly.count(x))