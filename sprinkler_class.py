class station:
    def __init__(self, name='Station', enabled=False):
        self.name = name
        self.enabled = enabled

    def myfunc(self):
        print("Hello my name is " + self.name)


class cycle:
    def __init__(self, number, startTime, daysOfWeek = [], stations = [], durations = [], enabled=False):
        self.number = number
        self.startTime = startTime
        self.daysOfWeek = list(daysOfWeek)
        self.stations = list(stations)
        self.durations = list(durations)
        self.enabled = enabled

    def getValues(self):
        values = [self.number, self.startTime, self.daysOfWeek, self.stations, self.durations, self.enabled]
        return values