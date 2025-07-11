class Player:

    def __init__(self):
        
        self.dead = false
        self.threat = 0

    def get_threat(self):
        return self.threat

    def is_dead(self):
        return self.dead

    def inc_threat(self):
        self.threat += 1

    def dec_threat(self):
        self.threat -= 1

    def set_threat(self, threat: int):
        self.threat = threat

    def kill(self):
        self.dead = true
