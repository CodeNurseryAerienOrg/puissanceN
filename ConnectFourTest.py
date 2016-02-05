import unittest
from user import *
from game import *


class ConnectFourTest(unittest.TestCase):
    #
    #
    # Given: A user "Jessica"
    # When : User is transformed into a string
    # Then : "Jessica" string is returned
    def test_user_Jessica(self):
        # Given
        jessica = User("Jessica")
        # When
        toString = str(jessica)
        # Then
        self.assertEqual("Jessica", toString)
    
    
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
        
    # 
    # 
    # Given: A user "Robert" and a game with "Jessica"
    # When : "Robert" joins the game
    # Then : "Jessica" and "Robert" are the both players in the game
    def test_Robert_joins_a_game_with_Jessica(self):
        # Given
        robert = User("Robert")
        game = Game()
        jessica = User("Jessica")
        game.accepts(jessica)

        # When
        game.accepts(robert)
        
        # Then
        self.assertEqual([jessica, robert], game.players)
        
    # 
    # 
    # Given: A user "Patricia" and a game with two players
    # When : "Patricia" joins the game
    # Then : Game throws a TooManyPlayersException and player list stays the
    #          same
    def test_Patricia_joins_a_game_with_two_players(self):
        # Given
        patricia = User("Patricia")
        
        game = Game()
        robert = User("Robert")
        jessica = User("Jessica")
        game.accepts(jessica)
        game.accepts(robert)

        # When-Then
        with self.assertRaises(TooManyPlayersException):
            game.accepts(patricia)
        self.assertEqual([jessica, robert], game.players)
        
    
    #
    #
    # Play a turn
    #
    #
    
    # 
    # Scenario I: First player plays first shot 
    #
    def test_Jessica_plays_first_shot(self):
        # Given
        game = Game()
        jessica = User("Jessica")
        robert = User("Robert")
        game.accepts(jessica)
        game.accepts(robert)
        
        self.assertEqual(jessica, game.currentPlayer)

        # When
        game.play(jessica, 0)
        
        # Then
        self.assertEqual([jessica], game.getColumn(0))
        
        for i in range(1, 6):
            self.assertEqual([], game.getColumn(i))
        
        self.assertEqual(robert, game.currentPlayer)
    
    # 
    # Scenario II: Second player tries to play first shot 
    #
    # def test_Robert_tries_to_play_first_shot(self):
    #     # Given
    #     game = Game()
    #     jessica = User("Jessica")
    #     robert = User("Robert")
    #     game.accepts(jessica)
    #     game.accepts(robert)
        
    #     self.assertEqual(jessica, game.currentPlayer)

    #     # When-Then
    #     with self.assertRaises(NotPlayerTurnException):
    #         game.play(robert, 0)
        
    #     for i in range(0, 6):
    #         self.assertEqual([], game.getColumn(i))
        
    #     self.assertEqual(jessica, game.currentPlayer)

        

if __name__=="__main__":		
	unittest.main()