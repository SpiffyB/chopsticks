import unittest

import core


class TestChopsticks(unittest.TestCase):
    def test_split_correct1(self):
        g = core.Game(2,0,2,5,verbose=False)
        g.players[0].hands[0].alive_fingers = 1
        g.players[0].hands[1].alive_fingers = 3
        self.assertEqual(g.split(0,0,1,2,2), True)
        
    def test_split_correct2(self):
        g = core.Game(2,0,2,5,verbose=False)
        g.players[0].hands[0].alive_fingers = 1
        g.players[0].hands[1].alive_fingers = 3
        g.split(0,0,1,2,2)
        self.assertEqual(g.players[0].hands[1].alive_fingers, 2)
    
    def test_split_correct3(self):
        g = core.Game(2,0,2,5,verbose=False)
        g.players[0].hands[0].alive_fingers = 1
        g.players[0].hands[1].alive_fingers = 3
        g.split(0,0,1,2,2)
        self.assertEqual(g.players[0].hands[0].alive_fingers, 2)
    
    def test_split_to_zero(self):
        g = core.Game(2,0,2,5,verbose=False)
        g.players[0].hands[0].alive_fingers = 1
        g.players[0].hands[1].alive_fingers = 3
        self.assertEqual(g.split(0,0,1,0,2), False)
        
    def test_split_to_negative(self):
        g = core.Game(2,0,2,5,verbose=False)
        g.players[0].hands[0].alive_fingers = 1
        g.players[0].hands[1].alive_fingers = 3
        self.assertEqual(g.split(0,0,1,-1,2), False)
        
    def test_split_to_num_fingers(self):
        g = core.Game(2,0,2,5,verbose=False)
        g.players[0].hands[0].alive_fingers = 1
        g.players[0].hands[1].alive_fingers = 3
        self.assertEqual(g.split(0,0,1,5,2), False)
        
    def test_split_to_greater_num_fingers(self):
        g = core.Game(2,0,2,5,verbose=False)
        g.players[0].hands[0].alive_fingers = 1
        g.players[0].hands[1].alive_fingers = 3
        self.assertEqual(g.split(0,0,1,6,2), False)
    
    def test_split_to_zero2(self):
        g = core.Game(2,0,2,5,verbose=False)
        g.players[0].hands[0].alive_fingers = 1
        g.players[0].hands[1].alive_fingers = 3
        self.assertEqual(g.split(0,0,1,2,0), False)
        
    def test_split_to_negative2(self):
        g = core.Game(2,0,2,5,verbose=False)
        g.players[0].hands[0].alive_fingers = 1
        g.players[0].hands[1].alive_fingers = 3
        self.assertEqual(g.split(0,0,1,2,-1), False)
        
    def test_split_to_num_fingers2(self):
        g = core.Game(2,0,2,5,verbose=False)
        g.players[0].hands[0].alive_fingers = 1
        g.players[0].hands[1].alive_fingers = 3
        self.assertEqual(g.split(0,0,1,2,5), False)
        
    def test_split_to_greater_num_fingers2(self):
        g = core.Game(2,0,2,5,verbose=False)
        g.players[0].hands[0].alive_fingers = 1
        g.players[0].hands[1].alive_fingers = 3
        self.assertEqual(g.split(0,0,1,2,6), False)
    
    def test_split_negative_hand_1(self):
        g = core.Game(2,0,2,5,verbose=False)
        g.players[0].hands[0].alive_fingers = 1
        g.players[0].hands[1].alive_fingers = 3
        self.assertEqual(g.split(0,-1,1,2,2), False)
        
    def test_split_negative_hand_2(self):
        g = core.Game(2,0,2,5,verbose=False)
        g.players[0].hands[0].alive_fingers = 1
        g.players[0].hands[1].alive_fingers = 3
        self.assertEqual(g.split(0,0,-1,2,2), False)
        
    def test_split_out_of_range_hand_1(self):
        g = core.Game(2,0,2,5,verbose=False)
        g.players[0].hands[0].alive_fingers = 1
        g.players[0].hands[1].alive_fingers = 3
        self.assertEqual(g.split(0,2,1,2,2), False)
        
    def test_split_out_of_range_hand_2(self):
        g = core.Game(2,0,2,5,verbose=False)
        g.players[0].hands[0].alive_fingers = 1
        g.players[0].hands[1].alive_fingers = 3
        self.assertEqual(g.split(0,0,2,2,2), False)
    
    


if __name__ == '__main__':
    unittest.main()