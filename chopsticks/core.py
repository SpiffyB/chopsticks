'''
Created on 6 Sep 2019

@author: Tom
'''


class Hand:
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
        """Adds alive fingers to the hand"""
        if (move_type == "h" and self.alive_fingers == 0) or num_fingers == 0:
            return False
        elif num_fingers + self.alive_fingers >= self.total_fingers:
            self.is_alive = False
            self.alive_fingers = 0
            return True
        else:
            self.alive_fingers = self.alive_fingers + num_fingers
            return True


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
 
 
        
class Player:
    def __init__(self, player_id,num_hands, num_fingers):
        self.hands = [Hand(num_fingers) for x in range(num_hands)]
        self.id = player_id
        self.is_alive = True
        
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
    def get_next_move(self):
        """Gets the next move from the player"""
        #TODO Check if move is valid
        is_error = True
        while is_error:
            move = g.ui.get_user_input(self.id) 
            if move != "error" and move != "help":
                is_error = False 
                    
        return move
        
        
        
class Bot(Player):
    pass


class Game:
    def __init__(self, num_human_players, num_bot_players, num_hands, num_fingers, verbose=True):
        self.num_human_players = num_human_players
        self.num_bot_players = num_bot_players
        self.num_players = num_human_players + num_bot_players
        self.num_hands = num_hands
        self.num_fingers = num_fingers
        self.game_is_over = False
        self.ui  = CommandLine()
        
        self.players = [Human(x+1, num_hands, num_fingers) for x in range(num_human_players)]
        self.players += [Bot(x+1, num_hands, num_fingers) for x in range(num_bot_players)]
        
        if verbose == True:
            print("Humans: ", self.num_human_players, "\nBots: ", self.num_bot_players, 
                  "\nHands per Player: ", self.num_hands, "\nFingers per hand: ", self.num_fingers , "\n")
    
    
    
    def hit(self, attack_player_id, defend_player_id, recieving_hand, giving_hand):
        """hits a player's hand with the current player's hand"""
        
        if attack_player_id == defend_player_id and giving_hand == recieving_hand:
            return False
        
        is_valid_move = self.players[defend_player_id].hands[recieving_hand].add_fingers("h",self.players[attack_player_id].hands[giving_hand].alive_fingers)
        
        return is_valid_move

    
    def split(self, player_id, hand_1, hand_2, amount_1, amount_2):
        """Splits the fingers between two hands"""
        hand_1_fingers = self.players[player_id].hands[hand_1].alive_fingers
        hand_2_fingers = self.players[player_id].hands[hand_2].alive_fingers
        
        #TODO Check if move is valid
        
        self.players[player_id].hands[hand_1].alive_fingers = amount_1
        self.players[player_id].hands[hand_2].alive_fingers = amount_2
        
        return True
    
    
    
    def check_if_game_over(self):
        """Check if the game is over"""
        alive_count = 0
        for player in self.players:
            if player.is_alive == True:
                alive_count += 1
            if alive_count > 1:
                return False
        return True
    
    
    def play(self):
        """Game Loop"""
        i = 0
        while self.game_is_over == False:
            if self.players[i].check_if_alive() == True:
                self.ui.display_game_state()
                if isinstance(self.players[i], Human):
                    is_valid_move = False
                    while is_valid_move == False:
                        move = self.players[i].get_next_move()
                        if move[0] == "h":
                            is_valid_move = self.hit(i, move[1]-1, move[2]-1, move[3]-1)
                        elif move[0] == "s":
                            is_valid_move = self.split(i, move[1]-1, move[2]-1, move[3], move[4])
                            
                        
                        if is_valid_move == False:
                            print("Not A Valid Move")
    
                else:
                    move = ("h","1","1","1") #TODO Change this
                    print("Bots Move")
                    
            self.game_is_over = self.check_if_game_over()
            i+=1
            if(i >= self.num_players):
                i=0
        print("Game Over")
        
if __name__ == '__main__':
    g = Game(2,0,2,5)
    g.play()

        
        
        
        
        
        
        
        
        