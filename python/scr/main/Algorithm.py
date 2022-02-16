class Algorithm:
    def __init__(self):
        self.matchList = []
        self.mainMatrix = []

    def algoritmo(self, patternMatr, mainMatr):
        self.mainMatrix = mainMatr
        for x in range(4):
            print(patternMatr)
            print("----------------------------------")
            self.matchList += [self.scorri_tutta_la_matrice(patternMatr, mainMatr)]
            patternMatr = self.ruota_pattern(patternMatr)

        print(self.matchList)
        countMatch = 0
        for x in range(4):
            print(self.matchList[x])
            print(len(self.matchList[x]))
            countMatch += len(self.matchList[x])
        print("match totali: ", countMatch)
        print(self.matchList)

        return countMatch

    def cerca_pattern(self, patternMatr, mainMatr, i, j):
        if len(mainMatr) < (i + len(patternMatr)) or len(mainMatr[i]) < (j + len(patternMatr[0])):
            return False
        else:
            out = True
            for k in range(i, i + len(patternMatr)):
                for u in range(j, j + len(patternMatr[0])):
                    if patternMatr[k - i][u - j] != mainMatr[k][u]:
                        out = False
            return out

    def scorri_tutta_la_matrice(self, patternMatr, mainMatr):
        machList = []
        for i in range(0, len(mainMatr)):
            for j in range(0, len(mainMatr[0])):
                match = self.cerca_pattern(patternMatr, mainMatr, i, j)
                if match:
                    machList += [[i, j]]
        return machList

    def ruota_pattern(self, patternMatr):
        nuovoPattern = []
        for j in range(0, len(patternMatr[0])):
            lista = []
            for i in range(0, len(patternMatr)):
                lista += [patternMatr[len(patternMatr) - (i + 1)][j]]
            nuovoPattern += [lista]
        return nuovoPattern
