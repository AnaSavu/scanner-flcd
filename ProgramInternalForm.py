class PIF:
    def __init__(self):
        self.data = []

    def add(self, token, ST_pos):
        self.data.append([token, ST_pos])