from multiprocessing import Process, Pipe
import threading
import time
import copy

station_number = -1
cycles_left = {}


def shut_off_station(station):
    global pipe_connection
    print("Station", station, "has been shut off.")
    data_to_send = {"command": "station_off", "number": station}
    pipe_connection.send(data_to_send)

def turn_on_station(station):
    global pipe_connection
    print("Turned on Station", str(station))
    data_to_send = {"command": "station_on", "number": station}
    pipe_connection.send(data_to_send)

def set_timer(station, duration):
    global active_station
    active_station = threading.Timer(duration, shut_off_station, args=[station])
    return active_station

def check_cycles_left():
    global active_station
    if active_station.isAlive() == False:
        if cycles_left:
            if len(cycles_left['stations']) > 0:
                turn_on_station(cycles_left['stations'][0])
                set_timer(cycles_left['stations'][0], cycles_left['durations'][0]).start()
                cycles_left['stations'].pop(0)
                cycles_left['durations'].pop(0)
                if (len(cycles_left['stations']) == 0):
                    del cycles_left['stations']
                    del cycles_left['durations']
                    del cycles_left['command']


def Main(process_conn):
    global pipe_connection
    global cycles_left
    global active_station
    active_station = threading.Timer(1, shut_off_station, args=[1])
    pipe_connection = process_conn
    #timer1 = set_timer(1, 5)
    #timer1.start()
    count = 1
    while True:
        '''
        print(timer1.isAlive())
        time.sleep(1)
        if (timer1.isAlive() == False):
            count += 1
            timer1 = set_timer(count, 5)
            timer1.start()

        if (count % 3 == 0):
            time.sleep(1)
            print("Canceling Timer", count)
            timer1.cancel()
        '''
        if (process_conn.poll()):
            incoming_message = process_conn.recv()
            if (incoming_message['command'] == "cycle"):
                if not cycles_left:
                    cycles_left = copy.deepcopy(incoming_message)
                else:
                    process_conn.send({"command":"error", "message":"A cycle is already running."})
                    print("A cycle is already running.")
                    continue
                turn_on_station(cycles_left['stations'][0])
                set_timer(cycles_left['stations'][0], cycles_left['durations'][0]).start()
                cycles_left['stations'].pop(0)
                cycles_left['durations'].pop(0)
                if (len(cycles_left['stations']) == 0):
                    del cycles_left['stations']
                    del cycles_left['durations']
                    del cycles_left['command']
            else:
                process_conn.send({"command":"error", "message":"Something went wrong"})
        check_cycles_left()
        time.sleep(.001)
