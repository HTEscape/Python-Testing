class station:
    def __init__(self, name='Station', enabled=False):
        self.name = name
        self.enabled = enabled

    def myfunc(self):
        print("Hello my name is " + self.name)


class cycle:
    def __init__(self, number, stations = [], durations = []):
        self.number = number
        self.stations = list(stations)
        self.durations = list(durations)