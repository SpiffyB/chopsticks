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