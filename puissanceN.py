
class puissanceN():
	def __init__(self):
		self.players = []
		self.board   = [[" "]*8]*8
	def ajouterJoueur(self, name):
		self.players.append(name)
		
	def jouer(self, player, column):
		self.board = [["R"] + [" "]*7] + [[" "]*8]*7

