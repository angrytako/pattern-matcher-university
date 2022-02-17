import tkinter as tkt

from PIL import ImageTk

from ShowRandPattern import *
from SetPattern import *
from Algorithm import *
from SetView import *

resultPattern = 0


# algorithm of pattern matching
def pattern_match(control, numPatternLb, risLb, patternMatr, mainMatr):
    def inner():
        global resultPattern
        if (resultPattern != 0):
            reset_pattern()

        alg = Algorithm()
        totPatternFounded = alg.algoritmo(patternMatr, mainMatr)

        resultPattern = change_color(alg, arrowRightButton, arrowLeftButton, risLb, numPatternLb, totPatternFounded, randomPatternFrame)

    control['command'] = inner


if __name__ == "__main__":
    root = tkt.Tk()
    root.title('Python pattern matching')

    # background pic
    backgroundImage = tkt.PhotoImage(file=r"../img/background.png")
    # backgroundImage = backgroundImage.subsample(2, 1)
    label = tkt.Label(root, image=backgroundImage)
    label.place(x=-40, y=0)

    # Frame: used to organized more elements together
    mainFrame = tkt.Frame(root, highlightbackground="grey", highlightthickness=1, width=200, height=200)
    mainFrame.pack(padx=40, pady=40)

    # title lable
    titleLb = tkt.Label(mainFrame, bg="white", font=("Arial", 22), text="Inserisci un pattern da cercare!", width=60,
                        height=1, borderwidth=1, relief="ridge")
    # titleLb.pack(pady=20, expand=True, fill=tk.BOTH)
    titleLb.grid(row=0, column=0, columnspan=5)

    # the frames in which the random pattern and the setting pattern matrix will be displayed
    settingPatternFrame = tkt.Frame(mainFrame, width=150, height=100)  # left
    randomPatternFrame = tkt.Frame(mainFrame, width=150, height=100)  # right

    patternMatrix = setting_grid_show(settingPatternFrame)
    randomMatrix = show_random_pattern(randomPatternFrame)

    settingPatternFrame.grid(row=1, column=0, padx=30, pady=30)  # select LEFT frame (setting pattern)
    randomPatternFrame.grid(row=1, column=2, padx=30, pady=30, columnspan=3)  # select RIGHT frame (random pattern)

    # button for starting to pattern match
    startBtn = tkt.Button(mainFrame, bg="white", text="Trova corrispondenze", height=2)
    startBtn.grid(row=2, column=1)

    # result label
    risLb = tkt.Label(mainFrame, bg="white", font=("Arial", 16), text="Corrispondenze trovate: 0")
    risLb.grid(row=1, column=1)

    # numPattern label
    numPatternLb = tkt.Label(mainFrame, bg="white", font=("Arial", 16), text="Num pattern : 0")
    numPatternLb.grid(row=2, column=3)

    # arrow left with image
    picLeft = tkt.PhotoImage(file=r"../img/arrow_left.png")
    arrowLeftButton = tkt.Button(mainFrame, bg="white", text="Arrow left", image=picLeft, width=60, height=30)
    arrowLeftButton.grid(row=2, column=2)

    # arrow right with image
    picRight = tkt.PhotoImage(file=r"../img/arrow_right.png")
    arrowRightButton = tkt.Button(mainFrame, bg="white", text="Arrow right", image=picRight, width=60, height=30)
    arrowRightButton.grid(row=2, column=4)

    # button function linked to algorithm
    pattern_match(startBtn, numPatternLb, risLb, patternMatrix, randomMatrix)

    root.mainloop()
