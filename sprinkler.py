from flask import Flask, request
from sprinkler_class import station, cycle
from multiprocessing import Process, Pipe
import Station_Timers

app = Flask(__name__)
flask_conn, timers_conn = Pipe()

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/test')
def test():
    command_list = request.args.getlist('command')
    command_length = len(command_list)
    if (command_length > 0):
        flask_conn.send(command_list[0])
        result = flask_conn.recv()
        return result
    else:
        return "No Command supplied!"


if __name__ == '__main__':

    timer_process = Process(target=Station_Timers.Main, args=(timers_conn,))
    timer_process.start()

    station1 = station(1, 'Chads Station', True)
    print(station1.name, "active =", station1.enabled)
    station1.myfunc()

    cycle1 = cycle(1, '8:00', [2, 5, 7], [10, 9, 8], [1,2,3], True)
    cycle2 = cycle(2, '10:00', [1, 3, 5, 7], [100, 49, 20, 65], [9,8,5], False)
    cycle3 = cycle(3)

    print("Cycle 1 stations:", cycle1.stations)
    print("Cycle 1 durations:", cycle1.durations)
    print("Cycle 2 stations:", cycle2.stations)
    print("Cycle 2 durations:", cycle2.durations)
    print(cycle1.getValues())
    print(cycle2.getValues())
    print(cycle3.getValues())

    app.run(debug=False, threaded=True)