class ST:
    def __init__(self):
        self.st = {}
        self.index = 0

    def hashFunction(self, key):
        return key.length() % len(self.st)

    def add(self, symbol):
        key = -1
        hf = self.hashFunction(symbol)
        for key in self.st.keys():
            if self.st[key] == symbol:
                return key
        # key = list(self.st.keys())[list(self.st.values()).index(symbol)])
        if key == -1:
            self.index += 1
            self.st[self.index-1] = symbol
            return self.index -1
        else:
            return key

