class S:
    def __init__(self, fileName, Q, E):
        self.file = fileName
        self.Q = Q
        self.E = E

    def writeData(self):
        with open(self.file, "w") as f:
            for element in self.E:
                f.write("(" + self.Q[0] + ", " + element + ") -> " + self.Q[1] + ";")
                f.write("(" + self.Q[1] + ", " + element + ") -> " + self.Q[1] + ";")