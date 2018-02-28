class Clock(object):
    def __init__(self, hour, minute):
        self.minute = minute % 60
        self.hour = (hour + minute / 60) % 24

    def __repr__(self):
        return str('%02d' % self.hour) + ':' + str('%02d' % self.minute)

    def __eq__(self, other):
        return self.hour == other.hour and self.minute == other.minute:
        
    def __add__(self, minutes):
        self.hour = (self.hour + (self.minute + minutes) / 60) % 24
        self.minute = (self.minute + minutes) % 60
        return self

    def __sub__(self, minutes):
        self.hour = (self.hour + (self.minute - minutes) / 60) % 24
        self.minute = (self.minute - minutes) % 60
        return self

    def __str__(self):
        return str('%02d' % self.hour) + ':' + str('%02d' % self.minute)