# Stage class

class Stage:
    def __init__(self, ID, desc = "" : str):
        # information
        self.ID = ID
        self.description = desc
        self.neighbors = []
        self.actors = []
        self.props = []
