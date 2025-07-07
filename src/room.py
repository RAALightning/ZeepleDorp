# room class

class Room:
    def __init__(self,roomID, name : str, description : str):
        self.roomID = roomID
        self.name = name
        self.description = description
        self.neighbors = []
        self.occupants = []

    def get_ID(self):
        return self.roomID
    def get_name(self):
        return self.name
    def get_description(self):
        return self.description
    def get_neighbors(self):
        return self.neighbors
    def get_occupants(self):
        return self.occupants

    def connect(self, other_room):
        if other_room not in self.neighbors:
            self.neighbors.append(other_room.roomID)
        if self not in other_room.neighbors:
            other_room.neighbors.append(self.roomID)
