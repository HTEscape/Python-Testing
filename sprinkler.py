from flask import Flask
from sprinkler_class import station, cycle

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/test')
def test():

    return 'Something'


if __name__ == '__main__':
    station1 = station('Chads Station', True)
    print(station1.name, "active =", station1.enabled)
    station1.myfunc()

    cycle1 = cycle(1, [2, 5, 7], [10, 9, 8])
    cycle2 = cycle(2, [1, 3, 5, 7], [100, 49, 20, 65])

    print("Cycle 1 stations:", cycle1.stations)
    print("Cycle 1 durations:", cycle1.durations)
    print("Cycle 2 stations:", cycle2.stations)
    print("Cycle 2 durations:", cycle2.durations)

    app.run()