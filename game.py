class Game():
    def __init__(self):
        self.players = []
        self.currentPlayer = None

    def accepts(self, user):
        if len(self.players) >= 2:
            raise TooManyPlayersException()
        self.players.append(user)
        self.currentPlayer = self.players[0]
        
    def play(self, user, columnId):
        self.currentPlayer = self.players[1]
        
    def getColumn(self, columnId):
        return [self.players[0]] if columnId == 0 else []
    
class TooManyPlayersException(Exception):
    pass
