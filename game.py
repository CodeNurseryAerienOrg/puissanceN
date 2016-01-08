class Game():
    def __init__(self):
        self.players = []
    
    def accepts(self, user):
        if len(self.players) >= 2:
            raise TooManyPlayersException()
        self.players.append(user)
    
    
class TooManyPlayersException(Exception):
    pass
