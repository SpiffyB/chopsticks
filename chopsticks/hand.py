
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