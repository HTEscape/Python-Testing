from sprinkler_class import *
import json
from multiprocessing import Process, Pipe
import Station_Timers
import os.path
import datetime
import time

station_list = []
cycle_list = []
current_day_of_week = -1
current_hour = -1
current_minute = -1

sprinkler_conn, timers_conn = Pipe()


def check_start_times():
    for j in range(len(cycle_list)):
        if cycle_list[j].enabled:
            if (current_hour == cycle_list[j].startTimeHour) and (current_minute == cycle_list[j].startTimeMinute):
                data_to_send = {"command": "cycle", "stations": cycle_list[j].stations,
                                "durations": cycle_list[j].durations}
                sprinkler_conn.send(data_to_send)
                #received_data = sprinkler_conn.recv()
                #print(received_data)
                #print(cycle_list[j].name, "has Started")
                break

def update_time():
    global current_minute
    global current_hour
    time_now = datetime.datetime.now()
    if current_minute != time_now.minute:
        current_minute = time_now.minute
        if current_hour != time_now.hour:
            current_hour = time_now.hour
        check_start_times()


def check_pipes(flaskpipe):
    if (sprinkler_conn.poll()):
        incoming_message = sprinkler_conn.recv()
        if (incoming_message['command'] == "station_on"):
            station_list[incoming_message['number']-1].active = True
        elif (incoming_message['command'] == "station_off"):
            station_list[incoming_message['number']-1].active = False
        elif (incoming_message['command'] == "error"):
            print("The error message from the pipe is :" + incoming_message['message'])



def main(flask_pipe):
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
            cycle_temp = cycle(temp_list['number'], temp_list['name'], temp_list['start time hour'],
                               temp_list['start time minute'], temp_list['days of week'], temp_list['stations'],
                               temp_list['durations'], temp_list['enabled'])
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
        station_list[i].myfunc()
    for i in range(len(cycle_list)):
        print(cycle_list[i].getValues())

    timer_process = Process(target=Station_Timers.Main, args=(timers_conn,))
    timer_process.start()

    while True:
        update_time()
        check_pipes(flask_pipe)


if __name__ == '__main__':
    main(1)
