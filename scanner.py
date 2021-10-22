import re

def isOperator(token):
    operators = ["+", "-", "*", "/", "%", "=<", "=>", ">", "<", "=", "==", "=!", "+=", "-="]
    if token in operators:
        return True
    return False

def isSeparator(token):
    separators = ["(", ")", "{", "}", ":", ";", ",", " "]
    if token in separators:
        return True
    else:
        return False

def isIdentifier(token):
    return re.match('^[A-Za-z]([a-zA-Z]|[0-9])', token) is not None

def isConstant(token):
    return re.match('^|[1-9][0-9]*', token) is not None


def getComment(line, index):
    token = ''
    quoteCounter = 1

    while index < len(line) and quoteCounter < 2:
        token += line[index]
        index += 1

    return token, index

def getTokens(line):
    tokens = []
    token = ''
    index = 0

    while index < len(line):
        #check if line[index] + line[index+1] is operator
        checkOperator = line[index] + line[index+1]
        if isOperator(checkOperator):
            token += line[index] + line[index+1]
            index += 2
            continue
        elif isOperator(line[index]):
            token += line[index]
            index += 1
            continue
        #check if comment is the following
        elif line[index] == "\"":
            t, index = getComment(line, index+1)
            token += t
        else:
            tokens.append(token)
            token = ''


    return tokens






