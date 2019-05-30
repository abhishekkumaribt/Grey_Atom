'''# Created on May 30, 2019
 
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
 
manOfTheMatch = data['info']['player_of_match'][0]
runsByManOfTheMatch = 0
 
batsman1stInnings = Counter()
batsman1stInningsAll = Counter()
sixCount1stInnings = Counter()
 
extra1stInnings = 0
extra2ndInnings = 0
batsmanBowled2ndInnings = []
 
for deliveries in data['innings'][0]['1st innings']['deliveries']:
    if deliveries[list(deliveries.keys())[0]]['batsman'] == manOfTheMatch:
        runsByManOfTheMatch += deliveries[list(deliveries.keys())[0]]['runs']['batsman']
    batsman1stInnings.update([deliveries[list(deliveries.keys())[0]]['batsman']])
    batsman1stInningsAll.update([deliveries[list(deliveries.keys())[0]]['batsman']])
    batsman1stInningsAll.update([deliveries[list(deliveries.keys())[0]]['non_striker']])
    if deliveries[list(deliveries.keys())[0]]['runs']['batsman'] == 6:
        sixCount1stInnings.update([deliveries[list(deliveries.keys())[0]]['batsman']])
    if 'extras' in deliveries[list(deliveries.keys())[0]].keys():
        extra1stInnings += 1
 
for deliveries in data['innings'][1]['2nd innings']['deliveries']:
    if deliveries[list(deliveries.keys())[0]]['batsman'] == manOfTheMatch:
        runsByManOfTheMatch += deliveries[list(deliveries.keys())[0]]['runs']['batsman']
    if 'extras' in deliveries[list(deliveries.keys())[0]].keys():
        extra2ndInnings += 1
    if 'wicket' in deliveries[list(deliveries.keys())[0]].keys() and deliveries[list(deliveries.keys())[0]]['wicket']['kind'] == 'bowled':
        batsmanBowled2ndInnings.append(deliveries[list(deliveries.keys())[0]]['batsman'])
 
ballFacedBySCGanguly = batsman1stInnings.get("SC Ganguly")
batsmanWithMostSixes = sixCount1stInnings.most_common(1)[0][0]
batsmanWithMostSixesCount = sixCount1stInnings.most_common(1)[0][1]
 
print("Total no of ball Faced By SC Ganguly:", ballFacedBySCGanguly)
print(manOfTheMatch, "was man of match and he scored", runsByManOfTheMatch, "runs")
print("Batsman played in 1st innings are", ", ".join(list(batsman1stInningsAll.keys())))
print(batsmanWithMostSixes, "hitted", batsmanWithMostSixesCount, "which was maximun in the match")
print("Batsman bowled in 2nd innings are ", ", ".join(batsmanBowled2ndInnings))
print(extra2ndInnings-extra1stInnings, "more extra balls were bownled in second innings")