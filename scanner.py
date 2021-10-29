import re

class Scanner:
    def __init__(self, st, pif, tokenFile, programFile):
        self.st = st
        self.pif = pif
        self.operators, self.separators, self.reservedWords = self.readTokens(tokenFile)
        self.fileName = programFile

    def getTokens(self):
        return self.operators, self.separators, self.reservedWords

    def getST(self):
        return self.st.getST()

    def getPIF(self):
        return self.pif.getData()

    def readLine(self, line):
        words = []
        x = ''
        for char in line:
            if char == " ":
                words.append(x)
                x = ''
            else:
                x += char
        new = re.sub(r'\n', '', x)
        words.append(new)
        return words

    def readTokens(self, fileName):
        file = open(fileName, "r")
        operators, separators, reservedWords = [], [], []
        lineCounter = 0
        for line in file:
            if lineCounter == 0:
                operators = self.readLine(line)
            elif lineCounter == 1:
                separators = self.readLine(line)
                index = separators.index("\\n")
                separators[index] = "\n"
                index = separators.index("\\t")
                separators[index] = "\t"
                separators.append(" ")
            else:
                reservedWords = self.readLine(line)
            lineCounter += 1


        return operators, separators, reservedWords


    def isPartOfOperator(self, char):
        # operators = ["+", "-", "*", "/", "%", "=<", "=>", ">", "<", "=", "==", "=!", "+=", "-="]
        operators = self.operators
        for op in operators:
            if char in op:
                return True
        return False

    def isOperator(self, token):
        # operators = ["+", "-", "*", "/", "%", "=<", "=>", ">", "<", "=", "==", "=!", "+=", "-="]
        operators = self.operators
        if token in operators:
            return True
        return False

    def isSeparator(self, token):
        # separators = ["(", ")", "{", "}", ":", ";", ",", "\n", "\t", "\"", " "]
        separators = self.separators
        if token in separators:
            return True
        else:
            return False

    def isReservedWord(self, token):
        reservedWords = self.reservedWords
        if token in reservedWords:
            return True
        return False

    def isIdentifier(self, token):
        return re.match('^[A-Za-z]([a-zA-Z]|[0-9])*', token) is not None

    def isConstant(self, token):
        return re.match('^(?:0|[1-9][0-9]*)$', str(token)) is not None

    def isStringConstant(self, token):
        return re.match('^"[A-Za-z]([a-zA-Z]|[0-9]|[:-><@#$])*', token) is not None

    def getComment(self, line, index):
        token = ''
        quoteCounter = 1

        while index < len(line) and quoteCounter < 2:
            if line[index] == "\"":
                return token, index
            token += line[index]
            index += 1

        return -1, -1

    def writeST(self):
        file = open("ST.out", "w")
        for i in range(len(self.st.getST())):
            if len(self.st.getST()[i]) == 0:
                file.write(str(self.st.getST()[i]) + "\n")
            else:
                list = []
                list.append(str(self.st.getST()[i][0]))
                file.write(str(list) + "\n")
        #file.write(str(self.getST()))
        file.close()

    def writePIF(self):
        file = open("PIF.out", "w")
        for i in range(len(self.pif.getData())):
            file.write(str(self.pif.getData()[i]) + "\n")
        #file.write(str(self.getPIF()))
        file.close()


    def scan(self):
        file = open(self.fileName, "r")
        lineNumber = 0
        # print(self.operators)
        # print(self.separators)
        # print(self.reservedWords)

        for line in file:
            generatedTokens = self.tokenGenerator(line, lineNumber)
            for i in range(len(generatedTokens)):
                if generatedTokens[i] == "":
                    continue
                if self.isReservedWord(generatedTokens[i]):
                    self.pif.add(generatedTokens[i], -1)
                elif self.isOperator(generatedTokens[i]):
                    if generatedTokens[i] == "-" and self.isConstant(generatedTokens[i+1]):
                        print("Lexical error on line number " + str(lineNumber) + "! Undefined negative number " + generatedTokens[i] + str(generatedTokens[i+1]) + "!")
                        return
                    else:
                        self.pif.add(generatedTokens[i], -1)
                elif self.isSeparator(generatedTokens[i]):
                        if generatedTokens[i] == " " or generatedTokens[i] == "\n" or generatedTokens[i] == "\t":
                            continue
                        else:
                            self.pif.add(generatedTokens[i], -1)
                elif self.isIdentifier(generatedTokens[i]):
                    key, st_pos = self.st.add(generatedTokens[i])
                    self.pif.add("identifier", (key, st_pos))
                elif self.isConstant(generatedTokens[i]):
                    key, st_pos = self.st.add(generatedTokens[i])
                    self.pif.add("constant", (key, st_pos))
                elif self.isStringConstant(generatedTokens[i]):
                    key, st_pos = self.st.add(generatedTokens[i])
                    self.pif.add("constant", (key, st_pos))
                else:
                    print("Lexical error on line number " + str(lineNumber) + "! Undefined token " + generatedTokens[i] + "!")
                    return
            lineNumber += 1

        print("Lexically correct!")
        self.writePIF()
        self.writeST()

        return



    def tokenGenerator(self, line, lineNumber):
        tokens = []
        token = ''
        index = 0
        while index < len(line):

            if self.isPartOfOperator(line[index]):
                if self.isPartOfOperator(line[index+1]):
                    if self.isOperator(line[index] + line[index+1]):
                        tokens.append(token)
                        token = ''
                        tokens.append(line[index] + line[index+1])
                        index += 2

                    else:
                        print("Lexical error on line number: " + lineNumber + " at token: " + line[index+1])
                        return
                else:
                    tokens.append(token)
                    token = ''
                    tokens.append(line[index])
                    index += 1

            elif line[index] == "\"":
                t, index = self.getComment(line, index+1)
                if (t, index) == (-1, -1):
                    print("Lexical error on line number: " + str(lineNumber))
                    return
                tokens.append(token)
                tokens.append("\"" + t + "\"")
                token = ''
                # tokens.append(t)
                # tokens.append("\"")
                index += 1

            elif self.isSeparator(line[index]):
                tokens.append(token)
                token = ''
                tokens.append(line[index])
                index += 1

            else:
                token += line[index]
                index += 1

        tokens.append(token)

        return tokens






