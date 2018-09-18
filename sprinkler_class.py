class station:
    def __init__(self, number, name='Station', enabled=True):
        self.number = number
        self.name = name
        self.active = False
        self.enabled = enabled

    def myfunc(self):
        print("Hello my name is " + self.name)

    def turnOn(self):
        self.active = True

    def turnOff(self):
        self.active = False


class cycle:
    def __init__(self, number, name, startTimeHour, startTimeMinute, daysOfWeek, stations, durations, enabled=False):
        self.number = number
        self.name = name
        self.startTimeHour = startTimeHour
        self.startTimeMinute = startTimeMinute
        self.daysOfWeek = list(daysOfWeek)
        self.stations = list(stations)
        self.durations = list(durations)
        self.enabled = enabled
        self.totalDuration = sum(self.durations)

    def getValues(self):
        values = [self.number, self.name, self.startTimeHour, self.startTimeMinute, self.daysOfWeek, self.stations, self.durations, self.enabled]
        return values
