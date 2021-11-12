#E - epsilon
#S - delta
import itertools


class FA:
    def __init__(self, fileName):
        self.Q = None
        self.E = None
        self.S = None
        self.q0 = None
        self.F = None
        self.readFromFileAndVerify(fileName)

    def eliminateDuplicates(self, x):
        temp_set = set(x)
        return list(temp_set)

    def determineTransitions(self, parts, Q, E):
        result = []
        transitions = []
        index = 0

        while index < len(parts):
            transitions.append(parts[index])
            index += 1

        for transition in transitions:
            lhs, rhs = transition.split('->')
            state2 = rhs.strip()

            if state2 not in Q:
                raise Exception(state2 + " is not in the set of states!")

            state1, route = [value.strip() for value in lhs.strip()[1:-1].split(',')]

            if state1 not in Q:
                raise Exception(state1 + " is not in the set of states!")
            if route == "":
                raise Exception("Transition of " + state1 + " and empty set is not allowed!")
            if route not in E:
                raise Exception(route + " is not defined in the alphabet!")

            result.append(((state1, route), state2))

        return result

    def transformLine(self, line):
        return [value.strip() for value in line.split('=')[1].strip()[1:-1].strip().split(';')]

    def readFromFileAndVerify(self, fileName):
        with open(fileName) as file:
            Q = self.transformLine(file.readline())
            Q = self.eliminateDuplicates(Q)

            E = self.transformLine(file.readline())
            E = self.eliminateDuplicates(E)

            for element in Q:
                if element in E:
                    raise Exception("The set of states cannot have elements of the alphabet!")

            try:
                S = self.determineTransitions(self.transformLine(file.readline()), Q, E)
            except Exception as e:
                print(e)
                exit()

            S = self.eliminateDuplicates(S)

            q0 = self.transformLine(file.readline())
            q0 = self.eliminateDuplicates(q0)

            if len(q0) != 1:
                raise Exception("There are more the one initial state!")
            if q0[0] not in Q:
                raise Exception("The initial state is not in the set of states!")

            F = self.transformLine(file.readline())
            F = self.eliminateDuplicates(F)

            for state in F:
                if state not in Q:
                    raise Exception("State " + state + " is not in the set of states!")

            self.setQ(Q)
            self.setE(E)
            self.setS(S)
            self.setq0(q0)
            self.setF(F)

    # return the set of states
    def getQ(self):
        return self.Q

    # return the alphabet
    def getE(self):
        return self.E

    # return all the transitions
    def getS(self):
        return self.S

    # return the set of final states
    def getF(self):
        return self.F

    def setQ(self, Q):
        self.Q = Q

    def setE(self, E):
        self.E = E

    def setS(self, S):
        self.S = S

    def setq0(self, q0):
        self.q0 = q0

    def setF(self, F):
        self.F = F

    def isDFA(self):
        for a, b in itertools.combinations(self.S, 2):
            if a[0] == b[0]:
                raise Exception("It is not DFA!")
            # print(a[0], end="")
            # print(b[0])
            # compare(a[0], b[0])

    def isSequenceAcceptedByFA(self, sequence):
        currentState = self.q0[0]

        for i in range(len(sequence)):
            posi = sequence[i]
            ok = 0
            for transition in self.S:
                if transition[0][1] == posi and transition[0][0] == currentState:
                    currentState = transition[1]
                    ok = 1
                    break
            if ok == 0:
                raise Exception("Sequence is not accepted by the FA!")

        if currentState not in self.F:
            raise Exception("Sequence is not accepted by the FA!")

    def toString(self):
        return "Q: " + str(self.Q) + "\n" + "E: " + str(self.E) + "\n" + "S: " + str(self.S) + "\n" + "q0: " + str(self.q0) + "\n" + "F: " + str(self.F)


