

class BusTime:

    def __init__(self, time_str = None, h = None, m = None, s = None):
        if time_str is not None:
            t = time_str.split(':')
            self.hour = int(t[0])
            self.minute = int(t[1])
            self.second = int(t[2])
        elif h is not None:
            self.hour = h
            self.minute = m
            self.second = s
        else:
            self.hour = s // 3600
            self.minute = (s - self.hour * 3600)//60
            self.second = s % 60

    def __add__(self, other):
        if isinstance(other, BusTime):
            s = self.seconds() + other.seconds()
            return BusTime(s=s)
        elif isinstance(other, int):
            s = self.seconds() + other
            return BusTime(s=s)
        else:
            raise TypeError("Unsupported operand type(s) for +: 'BusTime' and '{}'".format(type(other)))

    def __sub__(self, other):
        if isinstance(other, BusTime):
            s = self.seconds() - other.seconds()
            return BusTime(s=s)
        else:
            raise TypeError("Unsupported operand type(s) for +: 'BusTime' and '{}'".format(type(other)))

    def __ge__(self, other):
        if isinstance(other, BusTime):
            if self.hour > other.hour:
                return True
            elif self.hour == other.hour:
                if self.minute > other.minute:
                    return True
                elif self.minute == other.minute:
                    return self.second >= other.second
        else:
            raise TypeError("Unsupported operand type(s) for +: 'BusTime' and '{}'".format(type(other)))

    def __lt__(self, other):
        if isinstance(other, BusTime):
            if self.hour < other.hour:
                return True
            elif self.hour == other.hour:
                if self.minute < other.minute:
                    return True
                elif self.minute == other.minute:
                    return self.second < other.second
        else:
            raise TypeError("Unsupported operand type(s) for +: 'BusTime' and '{}'".format(type(other)))

    def __le__(self, other):
        if isinstance(other, BusTime):
            return self > other or self == other
        else:
            raise TypeError("Unsupported operand type(s) for +: 'BusTime' and '{}'".format(type(other)))

    def __eq__(self, other):
        if isinstance(other, BusTime):
            return self.hour == other.hour and self.minute == other.minute and self.second == other.second
        else:
            raise TypeError("Unsupported operand type(s) for +: 'BusTime' and '{}'".format(type(other)))

    def seconds(self):
        return self.hour * 60 * 60 + self.minute * 60 + self.second

    def __str__(self):
        return f'{self.hour}:{self.minute}:{self.second}'