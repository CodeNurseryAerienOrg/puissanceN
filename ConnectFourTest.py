import unittest
from user import *
from game import *


class ConnectFourTest(unittest.TestCase):
    # 
    # 
    # Given: A user "Jessica" and a new game
    # When : "Jessica" joins the game
    # Then : "Jessica" is the sole player in the game
    def test_Jessica_joins_a_new_game(self):
        # Given
        jessica = User("Jessica")
        game = Game()
        # When
        game.accepts(jessica)
        # Then
        self.assertEqual([jessica], game.players)

if __name__=="__main__":		
	unittest.main()