import json


sorting_order = {'Strength': 0, 'Defense': 1, 'Magic': 2, 'Health': 3, 'Slots': 4, 'Other': 5}
race_order = {'Clavat': 0, 'Selkie': 1, 'Lilty': 2, 'Yuke': 3}

with open('items.txt', 'r') as file:
    data = json.load(file)

items = data
#print(artifacts)
#This is the data I want to sort. It's the information stored inside of items.txt
"""
dictionary_list = [{'Ashura':
                    {'stat': 'Strength',
                     'value': 1,
                     'locations':
                        ['Tida, Cycle 1',
                         'Moschet Manor, Cycle 1',
                         'Veo Lu Sluice, Cycle 1',
                         'Lynari Desert, Cycle 1',
                         'Goblin Wall, Cycle 1/2',
                         'Selepation Cave, Cycle 1',
                         'The Mushroom Forest, Cycle 3',
                         'Toadstool Forest',
                         'Pale Cave']},
                   'Candy Ring':
                    {'stat': 'Magic',
                     'value': 1,
                     'locations':
                         ['Conall Curach, Cycle 1/2',
                          'Moschet Manor, Cycle 2/3',
                          'Daemon\'s Court, Cycle 1/2',
                          'Goblin Wall, Cycle 3',
                          'Veo Lu Sluice, Cycle 3',
                          'Afternoon Fort',
                          'The Goblin Festival']},
                    'Double Axe':
                        {'stat': 'Strength',
                         'value': 1,
                         'locations':
                         ['Daemon\'s Court, Cycle 1/2',
                          'Goblin Wall, Cycle 1/2',
                          'The Mushroom Forest, Cycle 1/2/3',
                          'The Mine of Cathuriges, Cycle 1/2',
                          'Lynari Desert, Cycle 1/2',
                          'River Belle Path, Cycle 1/2'
                          'Toadstool Forest']},
                    'Murasame':
                        {'stat': 'Strength',
                         'value': 4,
                         'locations':
                         ['The Mine of Cathuriges, Cycle 3',
                          'Miasma Pit',
                          'The Goblin Festival']},
                    'Shuriken':
                        {'stat': 'Strength',
                         'value': 1,
                         'locations':
                         ['River Belle Path, Cycle 1/3',
                          'Goblin Wall, Cycle 1',
                          'The Mushroom Forest, Cycle 1',
                          'The Mine of Cathuriges, Cycle 1',
                          'Moschet Manor, Cycle 1',
                          'Rebene Te Ra, Cycle 1',
                          'Tida, Cycle 1',
                          'Veo Lu Sluice, Cycle 1/2',
                          'Daemon\'s Court, Cycle 1',
                          'The Goblin Festival',
                          'Falling Leaves Path']},
                    'Maneater':
                        {'stat': 'Strength',
                         'value': 1,
                         'locations':
                         ['River Belle Path, Cycle 1/3',
                          'Goblin Wall, Cycle 1',
                          'The Mushroom Forest, Cycle 1/2',
                          'The Mine of Cathuriges, Cycle 1/2',
                          'Tida, Cycle 1/2',
                          'Conall Curach, Cycle 1',
                          'Daemon\'s Court, Cycle 1/2',
                          'Falling Leaves Path',
                          'Moonlit Desert',
                          'Oblivion Village',
                          'Rainy Ruins']},
                    'Kaiser Knuckles':
                        {'stat': 'Strength',
                         'value': 1,
                         'locations':
                         ['Tida, Cycle 1/2',
                          'Moschet Manor, Cycle 1/2',
                          'Veo Lu Sluice, Cycle 1',
                          'Conall Curach, Cycle 1',
                          'Goblin Wall, Cycle 1',
                          'Selepation Cave, Cycle 1/2',
                          'The Mine of Cathuriges, Cycle 3',
                          'Moonlit Desert',
                          'Oblivion Village']},
                    'Flametongue':
                        {'stat': 'Strength',
                         'value': 2,
                         'locations':
                         ['Moschet Manor, Cycle 1/2',
                          'Kilanda, Cycle 1/2/3',
                          'River Belle Path, Cycle 2/3',
                          'Goblin Wall, Cycle 2/3',
                          'The Mushroom Forest, Cycle 1/2/3',
                          'The Mine of Cathuriges, Cycle 2/3',
                          'Conall Curach, Cycle 1/2/3',
                          'Rebena Te Ra, Cycle 1',
                          'Lynari Desert, Cycle 1',
                          'Tida, Cycle 2/3',
                          'Daemon\'s Court, Cycle 3',
                          'Falling Leaves Path',
                          'Misty Mountain Kilanda',
                          'Moonlit Desert',
                          'Oblivion Village']},
                    'Ice Brand':
                        {'stat': 'Strength',
                         'value': 2,
                         'locations':
                         ['Tida, Cycle 1/2',
                          'Rebena Te Ra, Cycle 1/2',
                          'River Belle Path, Cycle 1/2/3',
                          'Goblin Wall, Cycle 2/3',
                          'The Mushroom Forest, Cycle 2/3',
                          'The Mine of Cathuriges, Cycle 2/3',
                          'Lynari Desert, Cycle 1/2/3',
                          'Veo Lu Sluice, Cycle 1',
                          'Conall Curach, Cycle 1/2',
                          'Moschet Manor, Cycle 2/3',
                          'Daemon\'s Court, Cycle 3',
                          'Afternoon Fort',
                          'The Dinner Party',
                          'Toadstool Forest']},
                    'Loaded Dice':
                        {'stat': 'Strength',
                         'value': 2,
                         'locations':
                         ['Conall Curach, Cycle 1/2',
                          'Lynari Desert, Cycle 1/2/3',
                          'River Belle Path, Cycle 2/3',
                          'Goblin Wall, Cycle 3',
                          'The Mushroom Forest, Cycle 3',
                          'The Mine of Cathuriges, Cycle 1/3',
                          'Daemon\'s Court, Cycle 1',
                          'Rebena Te Ra, Cycle 1/2',
                          'Veo Lu Sluice, Cycle 2/3',
                          'Selepation Cave, Cycle 3',
                          'Falling Leaves Path',
                          'Foggy Swamp',
                          'Miasma Pit',
                          'Pale Cave',]},
                    'Ogrekiller':
                        {'stat': 'Strength',
                         'value': 2,
                         'locations':
                         ['Tida, Cycle 2/3',
                          'Moschet Manor, Cycle 2/3',
                          'Veo Lu Sluice, Cycle 2/3',
                          'Lynari Desert, Cycle 2/3',
                          'Selepation Cave, Cycle 1/3',
                          'Daemon\'s Court, Cycle 2/3',
                          'Conall Curach, Cycle 2/3',
                          'Rebena Te Ra, Cycle 2/3',
                          'Frozen Sluice',
                          'Toadstool Forest']},
                    'Engetsurin':
                        {'stat': 'Strength',
                         'value': 2,
                         'locations':
                         ['Daemon\'s Court, Cycle 1/2',
                          'Kilanda, Cycle 1/2',
                          'Veo Lu Sluice, Cycle 2/3',
                          'Rebena Te Ra, Cycle 2/3',
                          'Tida, Cycle 3',
                          'Moschet Manor, Cycle 3',
                          'Goblin Wall, Cycle 2/3',
                          'Conall Curach, Cycle 3',
                          'Lynari Desert, Cycle 3',
                          'Moonlit Desert',
                          'Oblivion Village',
                          'The Dinner Party']}}]

"""

new_artifact = {'Futsu-no-Mitama':
                {'stat': 'Strength',
                 'value': 7,
                 'locations':
                 ['Foggy Swamp']}}

new_weapon = {
      'Queen\'s Heel': {
          'race': 'Selkie',
          'Strength': 33,
          'focus attack': 'Power Kick',
          'effect': None
      }
  }

new_main_armor = {'Bronze Plate':
                  {'race': 'All',
                   'Defense': 13,
                   'effect': None}}

if list(new_artifact.keys())[0] not in items[0].keys():
    items[0].update(new_artifact)

#print(items[1].keys())
#if list(new_weapon.keys())[0] not in items[1].keys():
#    items[1].update(new_weapon)

print(items[0].keys())
#print(items[1].keys())

items[0] = dict(sorted(items[0].items(), key=lambda x: (sorting_order.get(x[1]['stat']), x[1]['value'])))
#items[1] = dict(sorted(items[1].items(), key=lambda x: (race_order.get(x[1]['race']), x[1]['Strength'])))

#print(items[1].keys())
#items.append({'Copper Sword': {'race': 'Clavat', 'Strength': '15', 'focus attack': 'Power Slash'}})

#items.append({'Travel Clothes': {'race': 'All', 'Defense': 10, 'effect': None, 'value': None}})

#items.append({'Makeshift Shield': {'race': 'Clavat', 'Defense': 7, 'effect': None, 'value': None}})
#items.append({'Badge of the Flame': {'race': 'All', 'effect': 'Resist Fire', 'value': 1}})
#print(items[2])
#print(items[3])
#print(items[4])
with open('items.txt', 'w') as file:
    json.dump(items, file)









#I want my code to take the original list and sort it into a list
#of dictionaries. I want it to be sorted into artifacts_list.
#The way I want it sort is that I want them sorted first by their 'stat'
#value then next by their 'value' value.
"""
for key, outer_dict in dictionary_list:
    #I'm setting the 'stat' and 'value' from each dictionary to variables to use later
    stat = outer_dict['stat']
    value = outer_dict['value']
    #First, I sort by 'stat'. The first 'stat' will be 'Strength'
    if outer_dict['stat'] == 'Strength':
        #Starting a loop for 'Strength'
        for key2, inner_dict in artifacts_list[0]:
            #This checks if an entry for 'Strength' exists in artifacts_list
            #If the entry doesn't exist, then simply add the current artifact
            if not artifacts_list[0]:
                artifacts_list[0].add(outer_dict)
            #If an entry for 'Strength' already does exist, then I compare the 'value' values
            elif dict['value'] > outer_dict['value']:
                #If only one artifact exists and it's greater than
                #the artifact you want to add, put it in the
                #list before the existing artifact
                if key2.index == 0:
                    artifacts_list[0].prepend(outer_dict)
                #If multiple artifactss exist, then add insert it before
                #the artifact that is greater than itself
                else:
                    artifacts_list[0].insert(outer_dict, (key2.index-1))
    #Repeating the last loop but for if 'stat' is 'Defense'
    elif outer_dict['stat'] == 'Defense':
        for key2, inner_dict in artifacts_list[1]:
            if not artifacts_list[1]:
                artifacts_list[1].add(outer_dict)
            elif dict['value'] > outer_dict['value']:
                if key2.index == 0:
                    artifacts_list[1].prepend(outer_dict)
                else:
                    artifacts_list[1].insert(outer_dict, (key2.index-1))
    #Repeating the loop for if 'stat' is 'Magic'
    elif outer_dict['stat'] == 'Magic':
        for key2, inner_dict in artifacts_list[2]:
            if not artifacts_list[2]:
                artifacts_list[2].add(outer_dict)
            elif dict['value'] > outer_dict['value']:
                if key2.index == 0:
                    artifacts_list[2].prepend(outer_dict)
                else:
                    artifacts_list[2].insert(outer_dict, (key2.index-1))
    #Repeating for 'Health', 'Slot', and 'Spell'.
    #They will all have a 'value' value of 1,
    #so they don't need to need to be sorted
    #by 'value'
    elif outer_dict['stat'] == 'Health':
        artifacts_list[3].add(outer_dict)
    elif outer_dict['stat'] == 'Slot':
        artifacts_list[4].add(outer_dict)
    elif outer_dict['stat'] == 'Spell':
        artifacts_list[5].add(outer_dict)
"""


