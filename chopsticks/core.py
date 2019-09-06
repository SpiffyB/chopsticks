'''
Created on 6 Sep 2019

@author: Tom
'''

class Hand:
    def __init__(self, num_fingers):
        self.total_fingers = num_fingers
        self.alive_fingers = 1
        self.is_alive = True


class UserInterface:
    pass

class Gui:
    pass

class CommandLine:
    pass



class Player:
    def __init__(self, num_hands, num_fingers):
        self.hands = [Hand(num_fingers) for x in range(num_hands)]
        
        
class Human(Player):
    pass
    
class Bot(Player):
    pass