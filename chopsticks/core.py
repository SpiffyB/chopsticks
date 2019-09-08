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
    
    def get_user_input(self, player_id):
        """Gets the user input and returns the appropriate action or an error"""
        ui = input("Human " + str(player_id) + "'s turn: ")
        ui_list = ui.strip().lower().split()
        
        try:
            if ui_list[0] in ['h','hit']:
                #Input: Hit, PLayerBeingHit GivingHand, RecievingHand
                return ("h", ui_list[1], ui_list[2], ui_list[3])
            elif ui_list[0] in ['s','split']:
                #Input: Split, GivingHand, RecievingHand, Giving Amount
                return ("s", ui_list[1], ui_list[2], ui_list[3])
            elif ui_list[0] == "help":
                pass
            else:
                print("Not a Valid Command")
                return "error"
        except:
            print("Not a Valid Command")
            return "error"
 
 
        
class Player:
    def __init__(self, player_id,num_hands, num_fingers):
        self.hands = [Hand(num_fingers) for x in range(num_hands)]
        self.id = player_id
        
        
class Human(Player):
    def get_next_move(self):
        """Gets the next move from the player"""
        #TODO Check if move is valid
        is_error = True
        while is_error:
            move = g.ui.get_user_input(self.id) 
            if move != "error":
                is_error = False 
                    
        return move
        
        
        
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
    
    
    def hit(self, player_id, giving_hand, recieving_hand):
        pass
    
    def split(self, player_id, giving_hand, recieving_hand, giving_amount):
        pass
    
    
    
    
    def play(self):
        """Game Loop"""
        i = 0
        while self.game_is_over == False:
            self.ui.display_game_state()
            if isinstance(self.players[i], Human):
                move = self.players[i].get_next_move()
            else:
                move = ("h","1","1","1") #TODO Change this
                print("Bots Move")
            
            if move[0] == "h":
                self.hit(move[0], move[1], move[2])
            
            
            i+=1
            if(i >= self.num_players):
                i=0


if __name__ == '__main__':
    g = Game(2,0,2,5)
    g.play()

        
        
        
        
        
        
        
        
        