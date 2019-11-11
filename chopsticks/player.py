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