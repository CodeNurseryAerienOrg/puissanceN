import unittest
import puissanceN


class TestPuissanceN(unittest.TestCase):
	def setUp(self):
		self.game = puissanceN.puissanceN()
		
		
	def test_pas_de_joueur(self):
		self.assertEqual(self.game.players,[])
		
	def test_ajouter_joueur_Pascal(self):
		self.game.ajouterJoueur("Pascal")
		self.assertEqual(self.game.players,["Pascal"])
		
	def test_ajouter_joueur_Thierry(self):
		self.game.ajouterJoueur("Thierry")
		self.assertEqual(self.game.players,["Thierry"])
		
	def test_plateau(self):
		self.assertEqual(self.game.board, [[" "]*8]*8)
		
	def test_Stephane_joue_colonne_1(self):
		self.game.ajouterJoueur("Stéphane")
		self.game.jouer("Stéphane", 0)
		self.assertEqual(self.game.board, [["R"] + [" "]*7] + [[" "]*8]*7)
		
	def test_Stephane_joue_colonne_2(self):
		self.game.ajouterJoueur("Stéphane")
		self.game.jouer("Stéphane", 1)
		self.assertEqual(self.game.board, [[" "]*8] + [["R"] + [" "]*7] + [[" "]*8]*6)

	def test_Stephane_rejoue_colonne2(self):
		self.game.ajouterJoueur("Stéphane")
		self.game.jouer("Stéphane", 1)
		self.game.jouer("Stéphane", 1)
		self.assertEqual(self.game.board, [[" "]*8] + [["R"]*2 + [" "]*6] + [[" "]*8]*6)
		
	def test_colonne_remplie(self):
		self.game.ajouterJoueur("Stéphane")
		for i in range(8):
			self.game.jouer("Stéphane", 1)
		self.assertEqual(self.game.board, [[" "]*8] + [["R"]*8] + [[" "]*8]*6)

	def test_colonne_qui_deborde_lance_exception(self):
		self.game.ajouterJoueur("Stéphane")
		for i in range(8):
			self.game.jouer("Stéphane", 1)
		
		with self.assertRaises(puissanceN.ColonnePleineException):
			self.game.jouer("Stéphane", 1)
		
	def test_Jessica_joue_colonne_1(self):
		self.game.ajouterJoueur("Jessica")
		self.game.jouer("Jessica", 0)
		self.assertEqual(self.game.board, [["Y"] + [" "]*7] + [[" "]*8]*7)
    		
if __name__=="__main__":		
	unittest.main()