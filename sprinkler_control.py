from sprinkler_class import *
import json
from multiprocessing import Process, Pipe
import Station_Timers
import os.path

station_list = []
cycle_list = []


if os.path.isfile('sprinkler_config.json'):
    with open('sprinkler_config.json') as f:
        loaded_data = json.load(f)
    temp_list = []
    for i in range(len(loaded_data['stations'])):
        temp_list = loaded_data['stations'][i]
        station_temp = station(temp_list['number'], temp_list['name'], temp_list['enabled'])
        station_list.append(station_temp)

    for i in range(len(loaded_data['cycles'])):
        temp_list = loaded_data['cycles'][i]
        cycle_temp = cycle(temp_list['number'], temp_list['name'], temp_list['start time'], temp_list['days of week'],
                           temp_list['stations'], temp_list['durations'], temp_list['enabled'])
        cycle_list.append(cycle_temp)

    del temp_list

else:
    configuration = '''
    {
      "stations": [],
      "cycles": []
    }
    '''
    data = json.loads(configuration)
    with open('sprinkler_config.json', 'w') as outfile:
        json.dump(data, outfile, indent=2, sort_keys=True)

for i in range(len(station_list)):
    print(station_list[i].myfunc())
print(cycle_list[0].getValues())
