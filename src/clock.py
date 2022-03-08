class Hand:
    def __init__(self, pos):
        self.pos = pos # angle of hand from 12 o'clock
    
    def angle(self, other):
        return abs(self.pos - other.pos) 
    
class SecondHand(Hand):
    def __init__(self, pos):
        super().__init__(pos)
    
    def move(self):
        self.pos += 6

class MinuteHand(Hand):
    def __init__(self, pos):
        super().__init__(pos)
    
    def move(self):
        self.pos += 0.1

class HourHand(Hand):
    def __init__(self, pos):
        super().__init__(pos)
    
    def move(self):
        self.pos += 0.1 / 12

def verify(hour, minute, second):
    if abs(hour.angle(minute) - 120) <= 1 and abs(minute.angle(second) - 120) <= 1:
        return True
    if abs(hour.angle(second) - 120) <= 1 and abs(minute.angle(second) - 120) <= 1:
        return True
    return False

hour, minute, second = HourHand(0), MinuteHand(0), SecondHand(0)

for i in range(60*60*24):
    if verify(hour, minute, second): 
        print(hour.pos, minute.pos, second.pos)
        break
    hour.move()
    minute.move()
    second.move()

