'''
Created on 6 Sep 2019

@author: Tom
'''



class Hand:
    def __init__(self, num_fingers):
        self.total_fingers = num_fingers
        self.alive_fingers = 1
        self.is_alive = True


class Gui:
    pass

class CommandLine:
    """For Printing to the console"""
    def __init__(self):
        pass
    
    def display_game_state(self):
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
    
        
class Player:
    def __init__(self, player_id,num_hands, num_fingers):
        self.hands = [Hand(num_fingers) for x in range(num_hands)]
        self.id = player_id
        
        
class Human(Player):
    def get_next_move(self):
        move = input("Human " + str(self.id) + "'s turn: ")
    
class Bot(Player):
    pass


class Game:
    def __init__(self, num_human_players, num_bot_players, num_hands, num_fingers):
        self.num_human_players = num_human_players
        self.num_bot_players = num_bot_players
        self.num_players = num_human_players + num_bot_players
        self.num_hands = num_hands
        self.num_fingers = num_fingers
        self.game_is_over = False
        self.ui  = CommandLine()
        
        self.players = [Human(x+1, num_hands, num_fingers) for x in range(num_human_players)]
        self.players += [Bot(x+1, num_hands, num_fingers) for x in range(num_bot_players)]
        
        print("Humans: ", self.num_human_players, "\nBots: ", self.num_bot_players, 
              "\nHands per Player: ", self.num_hands, "\nFingers per hand: ", self.num_fingers , "\n")
    
    
    def hit(self, giving_hand, recieving_hand):
        pass
    
    def split(self, giving_hand, recieving_hand, giving_amount):
        pass
    
    
    
    
    def play(self):
        """Game Loop"""
        i = 0
        while self.game_is_over == False:
            self.ui.display_game_state()
            if isinstance(self.players[i], Human):
                self.players[i].get_next_move()
            else:
                print("Bots Move")
                
            i+=1
            
            if(i >= self.num_players):
                i=0

        
g = Game(2,0,2,5)
g.play()

        
        
        
        
        
        
        
        
        