"""
Created on 6 Sep 2019

Authors: Luca Bianchi 
         Tom MacArthur
"""

from chopsticks.player import Human, Bot, Player, Hand
import chopsticks.app.app as flapp
from abc import ABC, abstractmethod
import time


class Ui(ABC):
    """Abstract Class for the user interface"""
    def __init__(self):
        pass

    @abstractmethod
    def display_game_state(self, g):
        pass

    @abstractmethod
    def get_user_input(self, g, player_id):
        pass

class CommandLine(Ui):
    """For Printing to the console"""
    def __init__(self):
        pass
    
    def display_game_state(self, g):
        """Prints the number of fingers each player has"""
        str_list = []
        for player in g.players:
            if isinstance(player, Human):
                str_list.append( "Human " + str(player.id) + ": (")
            else:
                str_list.append( "Bot " + str(player.id) + ": (")
            
            for hand in player.hands:
                str_list.append(" " + str(hand.alive_fingers) + " ")
                
            str_list.append(")   |   ")
        print(''.join(str_list))
    
    def get_user_input(self, g, player_id):
        """Gets the user input and returns the appropriate action or an error"""
        ui = input("Human " + str(player_id) + "'s turn: ")
        ui_list = ui.strip().lower().split()
        
        try:
            if ui_list[0] in ['h','hit']:
                #Input: Hit, PLayerBeingHit RecievingHand, GivingHand
                return ("h",  int(ui_list[1]), int(ui_list[2]), int(ui_list[3]))
            elif ui_list[0] in ['s','split']:
                #Input: Split, Hand1, Hand2, Amount1, Amount2
                return ("s", int(ui_list[1]), int(ui_list[2]), int(ui_list[3]), int(ui_list[4]))
            elif ui_list[0] == "help":
                return "help"
            else:
                print("Not a Valid Command")
                return "error"
        except:
            print("Not a Valid Command")
            return "error"


class Gui(Ui):
    """Graphical user interface"""

    def __init__(self):
        self.fa = flapp.flask_app()
        self.fa.start()

    def display_game_state(self, g):
        self.fa.hello_world()

    def get_user_input(self, g, player_id):
        self.fa.hello_world()
        return ("h",1,1,1)