'''
Created on 6 Sep 2019

Authors: Luca Bianchi 
         Tom MacArthur

Description: Core functionality module for the Chopsticks game. Contains the game class
'''
from chopsticks.player import Human, Bot, Hand, Player
from chopsticks.user_interface import Ui, Gui, CommandLine
import chopsticks.logic as logic


class Game:
    """
    Class for running one instance of a game

    Parameters
    ----------
    num_human_players: int
        Number of human players
    num_bot_players: int
        Number of bot players
    num_hands: int
        Number of hands that each player has
    num_fingers: int
        Number of fingers that each hand has

    """
    def __init__(self, num_human_players, num_bot_players, num_hands, num_fingers):
        self.num_human_players = num_human_players
        self.num_bot_players = num_bot_players
        self.num_players = num_human_players + num_bot_players
        self.num_hands = num_hands
        self.num_fingers = num_fingers
        self.game_is_over = False
        self.logic = logic.Logic()
        self.ui  = Gui()
        
        self.players = [Human(x+1, num_hands, num_fingers) for x in range(num_human_players)]
        self.players += [Bot(x+1, num_hands, num_fingers) for x in range(num_bot_players)]
        
        print("Humans: ", self.num_human_players, "\nBots: ", self.num_bot_players, 
              "\nHands per Player: ", self.num_hands, "\nFingers per hand: ", self.num_fingers , "\n")

    
    def play(self):
        """Game Loop"""
        i = 0
        while self.game_is_over == False:
            if self.players[i].check_if_alive() == True:
                self.ui.display_game_state(self)
                if isinstance(self.players[i], Human):
                    is_valid_move = False
                    while is_valid_move == False:
                        move = self.players[i].get_next_move(self)
                        if move[0] == "h":
                            is_valid_move = self.logic.hit(self, i, move[1]-1, move[2]-1, move[3]-1)
                        elif move[0] == "s":
                            is_valid_move = self.logic.split(self, i, move[1]-1, move[2]-1, move[3], move[4])
                            
                        is_valid_move = True
                        if is_valid_move == False:
                            print("Not A Valid Move")
    
                else:
                    move = ("h","1","1","1") #TODO Change this
                    print("Bots Move")
                    
            self.game_is_over = self.logic.check_if_game_over(self)
            i+=1
            if(i >= self.num_players):
                i=0
            self.game_is_over = True
        print("Game Over")
        
if __name__ == '__main__':
    g = Game(2,0,2,5)
    g.play()

        
        
        
        
        
        
        
        
        
