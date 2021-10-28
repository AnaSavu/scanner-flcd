class ST:
    def __init__(self):
        self.buckets = []
        self.bucketCapacity = 15
        for i in range(self.bucketCapacity):
            self.buckets.append([])

    def hashFunction(self, key):
        sum = 0
        for character in key:
            sum += ord(character)
        return sum % self.bucketCapacity

    def add(self, symbol):
        #hash table
        index_key = self.hashFunction(symbol)

        #if bucket is empty
        if len(self.buckets[index_key]) == 0:
            self.buckets[index_key].append(symbol)
            return 0

        #if bucket not empty
        self.buckets[index_key].append(symbol)
        return len(self.buckets[index_key]) - 1

        # #unsorted table
        #
        # key = -1
        # for key in self.st.keys():
        #     if self.st[key] == symbol:
        #         return key
        # # key = list(self.st.keys())[list(self.st.values()).index(symbol)])
        # if key == -1:
        #     self.index += 1
        #     self.st[self.index-1] = symbol
        #     return self.index -1
        # else:
        #     return key

    def getST(self):
        return self.buckets

