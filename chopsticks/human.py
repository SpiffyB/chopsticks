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