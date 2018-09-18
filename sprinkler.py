from flask import Flask, request
from sprinkler_class import station, cycle
from multiprocessing import Process, Pipe
import sprinkler_control
import json

app = Flask(__name__)
flask_conn, sprinkler_conn = Pipe()

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


@app.route('/stations')
def stations():
    with open('sprinkler_config.json') as f:
        loaded_data = json.load(f)
    return json.dumps(loaded_data['stations'], sort_keys=True)


@app.route('/cycles')
def cycles():
    with open('sprinkler_config.json') as f:
        loaded_data = json.load(f)
    return json.dumps(loaded_data['cycles'], sort_keys=True)


if __name__ == '__main__':

    sprinklerControl = Process(target=sprinkler_control.main, args=(sprinkler_conn,))
    sprinklerControl.start()

    app.run(debug=False, threaded=True)
