from room import Room

class Actor:

    def __init__(self, location: Room = none):
        self.dead = False
        self.location = location

    def kill(self):
        if self.dead
            return    
        self.dead = True
        self.location = none
        # TODO remove from room

    def spawn(self,location):
        self.dead = false
        #TODO finish func
