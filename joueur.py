
__nextId__ = 0

def init():
    global __nextId__
    __nextId__ = 0
    
def getNextId():
    global __nextId__
    id = __nextId__
    __nextId__ += 1
    return id
    
class Joueur():
    
    def __init__(self):
        self.id = getNextId()
