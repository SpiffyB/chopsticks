"""
Created on 6 Sep 2019

Authors: Luca Bianchi 
         Tom MacArthur
"""

from abc import ABC, abstractmethod

class Hand:
    """
    Class representing the hand of a player
    """
    def __init__(self, num_fingers):
        self.total_fingers = num_fingers
        self.alive_fingers = 1
        self.is_alive = True
        
    def remove_fingers(self, num_fingers):
        """Removes fingers from the hands"""
        if self.alive_fingers - num_fingers >= 0:
            self.alive_fingers = self.alive_fingers - num_fingers
            return True
    
    def add_fingers(self, move_type, num_fingers):
        """
        Adds alive fingers to the hand
        
        Parameters
        ----------
        move_type: string
            Either "h" or "s"
        num_fingers: int
            Number of fingers to add
        """
        if (move_type == "h" and self.alive_fingers == 0) or num_fingers == 0:
            return False
        elif num_fingers + self.alive_fingers >= self.total_fingers:
            self.is_alive = False
            self.alive_fingers = 0
            return True
        else:
            self.alive_fingers = self.alive_fingers + num_fingers
            return True

class Player(ABC):
    """Abstract class for players in the game"""
    def __init__(self, player_id, num_hands, num_fingers):
        self.hands = [Hand(num_fingers) for x in range(num_hands)]
        self.id = player_id
        self.is_alive = True
    
    @abstractmethod
    def get_next_move(self,g):
        """Gets the next move"""
        pass

    def check_if_alive(self):
        """Checks if the player is alive"""
        if self.is_alive == False:
            return False
        
        for hand in self.hands:
            if hand.is_alive == True:
                return True
        self.is_alive = False
        return False

class Human(Player):
    """Class for human players"""
    def get_next_move(self,g):
        """Gets the next move from the player"""
        #TODO Check if move is valid
        is_error = True
        while is_error:
            move = g.ui.get_user_input(g, self.id) 
            if move != "error" and move != "help":
                is_error = False         
        return move

class Bot(Player):
    """Class for bot players"""
    def get_next_move(self,g):
        pass