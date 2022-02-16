def algoritmo(label, patternMatr, mainMatr):
    machList = []
    for x in range(4): 
        print(patternMatr)
        print("----------------------------------")
        machList += [scorriTuttaLaMatrice(patternMatr, mainMatr)]
        patternMatr = ruotaPattern(patternMatr)

    print(machList)
    countMatch = 0
    for x in range(4):
        print(machList[x])
        print(len(machList[x]))
        countMatch +=len(machList[x])
    print("match totali: ",countMatch)
    label['text']=("Corrispondenze trovate: ",countMatch)
    return machList
    
def cercaPattern(patternMatr, mainMatr,i,j):
    if (len(mainMatr) < (i+len(patternMatr)) or len(mainMatr[i]) < (j+len(patternMatr[0]))): 
        return False
    else:
        out = True
        for k in range(i,i+len(patternMatr)):
            for u in range(j,j+len(patternMatr[0])):
                if patternMatr[k-i][u-j]!=mainMatr[k][u]:
                    out=False
        return out


def scorriTuttaLaMatrice(patternMatr, mainMatr):
    machList = []
    for i in range(0,len(mainMatr)):
        for j in range(0,len(mainMatr[0])):
            match = cercaPattern(patternMatr, mainMatr,i,j)
            if match:
                machList += [[i,j]]
    return machList

def ruotaPattern(patternMatr):
    nuovoPattern=[]
    for j in range(0,len(patternMatr[0])):
        lista = []
        for i in range(0,len(patternMatr)):
            lista += [patternMatr[len(patternMatr)-(i+1)][j]]
        nuovoPattern += [lista]
    return nuovoPattern


            