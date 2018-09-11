from multiprocessing import Process, Pipe
import threading
import time

station_number = -1


def shut_off_station(station):
    print("Station", station, "has been shut off.")


def set_timer(station, duration):
    active_station = threading.Timer(duration, shut_off_station, args=[station])
    return active_station


def Main(process_conn):
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
            return_message = "I received your message."
            incoming_message = process_conn.recv()
            if (incoming_message == "data"):
                process_conn.send(return_message)
            elif ((incoming_message > '0') and (incoming_message < '9')):
                set_timer(int(incoming_message), 2).start()
                process_conn.send("A timer was set for station " + incoming_message)
            else:
                process_conn.send("Something went wrong")
        time.sleep(.001)