import unittest
import joueur

class TestJoueur(unittest.TestCase):
    
    def setUp(self):
        joueur.init()
    
    def test_premier_joueur_id_à_0(self):
        stéphane = joueur.Joueur()
        self.assertEqual(0, stéphane.id)
        
    def test_second_joueur_id_à_1(self):
        stéphane = joueur.Joueur()
        jessica = joueur.Joueur()
        self.assertEqual(1, jessica.id)
        
    		
if __name__=="__main__":		
	unittest.main()