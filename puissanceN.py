
class puissanceN():
	# board:
	#	8x8 array 
	# 	1st dimension: column
	#   2nd dimension: bottom-to-up rows
	def __init__(self):
		self.players = []
		self.board   = []
		for i in range(8):
			self.board.append([" "]*8)

	def ajouterJoueur(self, name):
		self.players.append(name)
		
	def jouer(self, player, column):
		self.board[column][0] = "R"

