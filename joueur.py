class JoueurFabrique():
    
    def __init__(self):
        self.nextId = 0
        
    def getNextId(self):
        id = self.nextId
        self.nextId += 1
        return id
        
    def creerJoueur(self):
        id = self.getNextId()
        joueur = Joueur(id)
        return joueur
    
class Joueur():
    
    def __init__(self, id):
        self.id = id
