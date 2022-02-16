import tkinter as tkt

from SetPattern import WIDTH, HEIGHT

totPatternFounded = 0
countPattern = 1
matchList = []
mainMatr = []
allPatterns = []
randomPatternFrame = []


def get_pattern(numPattern):
    posPattern = numPattern-1
    startX = allPatterns[posPattern][0]
    startY = allPatterns[posPattern][1]

    for i in range(0, WIDTH):
        for j in range(0, HEIGHT):
            if mainMatr[startX+i][startY+j]:
                label = tkt.Label(randomPatternFrame, bg="blue", width=2, height=1)
            else:
                label = tkt.Label(randomPatternFrame, bg="orange", width=2, height=1, borderwidth=1, relief="raised")
            label.grid(row=startX+i, column=startY+j)
    pass


def reset_pattern():
    posPattern = countPattern-1
    startX = allPatterns[posPattern][0]
    startY = allPatterns[posPattern][1]

    for i in range(0, WIDTH):
        for j in range(0, HEIGHT):
            if mainMatr[startX+i][startY+j]:
                label = tkt.Label(randomPatternFrame, bg="black", width=2, height=1)
            else:
                label = tkt.Label(randomPatternFrame, bg="white", width=2, height=1, borderwidth=1, relief="raised")
            label.grid(row=startX+i, column=startY+j)
    pass


def next_image(control, label):
    def inner():
        global countPattern
        if totPatternFounded > 0:
            if countPattern < totPatternFounded:
                reset_pattern()
                countPattern = countPattern + 1
                get_pattern(countPattern)
            return label.config(text="Num pattern : " + str(countPattern) + "/" + str(totPatternFounded))

    control['command'] = inner


def prev_image(control, label):
    def inner():
        global countPattern
        if totPatternFounded > 0:
            if countPattern > 1:
                reset_pattern()
                countPattern = countPattern - 1
                get_pattern(countPattern)
            return label.config(text="Num pattern : " + str(countPattern) + "/" + str(totPatternFounded))

    control['command'] = inner


def set_pattern():
    global matchList, allPatterns
    allPatterns = []

    for i in range(0, len(matchList)):
        if matchList[i] != []:
            for j in range(0, len(matchList[i])):
                allPatterns += [matchList[i][j]]
    pass


def change_color(alg, arrowRightButton, arrowLeftButton, risLb, numPatternLb, tot, frame):
    global totPatternFounded, countPattern
    totPatternFounded = tot
    countPattern = 1

    if totPatternFounded == 0:
        risLb.config(text="Nessuna corrispondenza trovata!")
        numPatternLb.config(text="Num pattern : 0")
        return 0

    else:
        risLb.config(text="Corrispondenze trovate: " + str(totPatternFounded))
        numPatternLb.config(text="Num pattern : " + str(countPattern) + "/" + str(totPatternFounded))

        # impost matchList, mainMatr and frame
        global matchList, mainMatr, randomPatternFrame
        matchList = alg.matchList
        mainMatr = alg.mainMatrix
        randomPatternFrame = frame

        # set all possible patterns into a single matrix (allPatterns)
        set_pattern()

        # set first pattern (countPattern = 1)
        get_pattern(countPattern)

        # next image
        next_image(arrowRightButton, numPatternLb)

        # prev image
        prev_image(arrowLeftButton, numPatternLb)
        return 1
