import unittest
import joueur

class TestJoueur(unittest.TestCase):
    
    def setUp(self):
        self.joueurFabrique = joueur.JoueurFabrique()
        
    def test_premier_joueur_id_à_0(self):
        stéphane = self.joueurFabrique.creerJoueur()
        self.assertEqual(0, stéphane.id)
        
    def test_second_joueur_id_à_1(self):
        stéphane = self.joueurFabrique.creerJoueur()
        jessica = self.joueurFabrique.creerJoueur()
        self.assertEqual(0, stéphane.id)
        self.assertEqual(1, jessica.id)
        
    		
if __name__=="__main__":		
	unittest.main()