"""
Created on 6 Sep 2019

Authors: Luca Bianchi 
         Tom MacArthur

Description: Object which contains the game logic
"""

class Logic:
    """
    Class for game logic
    """
    def hit(self, g, attack_player_id, defend_player_id, recieving_hand, giving_hand):
        """
        hits a player's hand with the current player's hand and updates the Game object g
        
        Parameters
        ----------
        g: Game object
            reference to the game object
        attack_player_id: int
            Id of the attacking player
        defend_player_id: int
            Id of the defending player
        recieving_hand: int
            Id of the hand of the defending player
        giving_hand: int
            Id of the hand of the attacking player

        Returns
        -------
        is_valid_move: bool
            True if the move is valid, otherwise false
        """
        
        #move validation
        if attack_player_id == defend_player_id and giving_hand == recieving_hand:
            return False
        
        defending_hand = g.players[defend_player_id].hands[recieving_hand]
        num_attacking_fingers = g.players[attack_player_id].hands[giving_hand].alive_fingers
        
        is_valid_move = defending_hand.add_fingers("h", num_attacking_fingers)
        
        return is_valid_move

    
    def split(self, g, player_id, hand_1, hand_2, amount_1, amount_2):
        """
        Splits the fingers between two hands and updates the Game object g
        
        Parameters
        ----------
        g: Game object
            reference to the game object
        player_id: int
            Id of the player
        hand_1: int
            First hand which is splitting
        hand_2: int
            Second hand which is splitting
        amount_1: int
            New number of fingers on hand 1
        amount_2: int
            New number of fingers on hand 2
            
        Returns
        -------
        is_valid_move: bool
            True if the move is valid, otherwise false
        """

        
        if hand_1 > g.num_hands - 1:
            print('Select a hand')
            return False
        if hand_2 > g.num_hands - 1:
            print('Select a hand')
            return False
        
        hand_1_fingers = g.players[player_id].hands[hand_1].alive_fingers
        hand_2_fingers = g.players[player_id].hands[hand_2].alive_fingers
        
       
        if hand_1_fingers + hand_2_fingers == 1:
            print('Cannot split.')
            return False
        elif hand_1_fingers == 1 and hand_2_fingers == 1:
            print('Must have more than one finger to split.')
            return False
        elif hand_1_fingers == amount_2 and hand_2_fingers == amount_1:
            print('This is the same hand set as before.')
            return False
        elif amount_1 == 0:
            print('Cannot destroy hand this way.')
            return False
        elif amount_2 == 0:
            print('Cannot destroy hand this way.')
            return False
        elif hand_1_fingers + hand_2_fingers != amount_1 + amount_2:
            print('Must equal same amount of fingers.')
            return False
        elif amount_1 >= g.num_fingers:
            print('Too many fingers on one hand.')
            return False
        elif amount_2 >= g.num_fingers:
            print('Too many fingers on one hand.')
            return False
        elif amount_1 <=0:
            print('Cannot have a negative')
            return False
        elif amount_2 <=0:
            print('Cannot have a negative')
            return False
        elif hand_1 == -1:
            print('Select a hand.')
            return False
        elif hand_2 == -1:
            print('Select a hand.')
            return False
        elif player_id >= g.num_players:
            print('Select someone who is playing.')
            return False
        elif player_id < 0:
            print('Select somone who is playing')
            return False
        else: 
            g.players[player_id].hands[hand_1].alive_fingers = amount_1
            g.players[player_id].hands[hand_2].alive_fingers = amount_2
            return True


    def check_if_game_over(self, g):
        """
        Check if the game is over
        
        Parameter
        ---------
        g: Game object
            reference to the game object

        Returns
        -------
        True if 2 or more players are alive, otherwise false
        """
        alive_count = 0
        for player in g.players:
            if player.is_alive == True:
                alive_count += 1
            if alive_count > 1:
                return False
        return True
    