# Actor class and its subclasses

class Actor:
    def __init__(self, ID, name, description = "" : str):
        self.ID = ID
        self.name = name
        self.description = description
        self.location = None
        self.inventory = []        


class PlayerCharacter(Actor):
    def __init__(self, ID, name, description = "" : str):
        super.__init__(ID, name, description)

        
class NPC(Actor):
    def __init__(self, ID, name, description = "" : str):
        super.__init__(ID, name, description)


class Monster(Actor):
    def __init__(self, ID, name, description = "" : str):
        super.__init__(ID, name, description)
