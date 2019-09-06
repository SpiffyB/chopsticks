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
        player_count = 1
        for player in g.players:
            if isinstance(player, Human):
                str_list.append( "Human " + str(player_count) + ": (")
            else:
                str_list.append( "Bot " + str(player_count) + ": (")
            
            for hand in player.hands:
                str_list.append(" " + str(hand.alive_fingers) + " ")
                
            str_list.append(")   |   ")
            player_count += 1
        
        print(''.join(str_list))
    
        
class Player:
    def __init__(self, num_hands, num_fingers):
        self.hands = [Hand(num_fingers) for x in range(num_hands)]
        
        
class Human(Player):
    def get_next_move(self):
        move = input("Your Turn: ")
    
class Bot(Player):
    pass


class Game:
    def __init__(self, num_human_players, num_bot_players, num_hands, num_fingers):
        self.num_human_players = num_human_players
        self.num_bot_players = num_bot_players
        self.num_players = num_human_players + num_bot_players
        self.num_hands = num_hands
        self.num_fingers = num_fingers
        self.is_over = False
        self.ui  = CommandLine()
        
        self.players = [Human(num_hands, num_fingers) for x in range(num_human_players)]
        self.players += [Bot(num_hands, num_fingers) for x in range(num_bot_players)]
    
    def play(self):
        """Game Loop"""
        i = 0
        while self.is_over == False:
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

        
        
        
        
        
        
        
        
        