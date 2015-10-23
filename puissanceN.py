class ColonnePleineException(Exception):
	pass

class puissanceN():
	# board:
	#	8x8 array 
	# 	1st dimension: column
	#   2nd dimension: bottom-to-up rows
	#
	#   ┌─────────┬─────────┬───────────────────────────────┐
	#   │         │ 2nd dim │                               │
	#   ├─────────┼─────────┼───┬───┬───┬───┬───┬───┬───┬───┤
	#   │         │       7 │   │   │   │   │   │   │   │   │
	#   │         │       6 │   │   │   │   │   │   │   │   │
	#   │         │       5 │   │   │   │   │   │   │   │   │
	#   │         │       4 │   │   │   │   │   │   │   │   │
	#   │         │       3 │   │   │   │   │   │   │   │   │
	#   │         │       2 │   │   │   │   │   │   │   │   │
	#   │         │       1 │   │   │   │   │   │   │   │   │
	#   │         │       0 │   │   │   │   │   │   │   │   │
	#   ├─────────┼─────────┼───┼───┼───┼───┼───┼───┼───┼───┤
	#   │ 1st dim │         │ 0 │ 1 │ 2 │ 3 │ 4 │ 5 │ 6 │ 7 │
	#   └─────────┴─────────┴───┴───┴───┴───┴───┴───┴───┴───┘
    #     
	def __init__(self):
		self.players = []
		self.board   = []
		for i in range(8):
			self.board.append([" "]*8)

	def ajouterJoueur(self, name):
		self.players.append(name)
		
	def jouer(self, player, column):
		for i in range(8):
			if self.board[column][i] == " ":
				self.board[column][i] = "Y" if player == "Jessica" else "R"
				return
		raise ColonnePleineException()


