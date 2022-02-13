import tkinter as tk
from ShowRandPattern import *
from SetPattern import *


# to be used in order to add the pattern_match as a callback to the button
def add_pattern_match_callback(control, label, patternMatr, mainMatr, fun):
    def inner():
        return fun(label, patternMatr, mainMatr)

    control['command'] = inner


# still has to be implemented
def pattern_match(label, patternMatr, mainMatr):
    print(patternMatr)
    pass


if __name__ == "__main__":
    root = tk.Tk()
    mainFrame = tk.Frame(root)
    mainFrame.pack()

    # title lable
    titleLb = tk.Label(mainFrame, bg="white", font=("Arial", 25), text="Inserisci un pattern da cercare!")
    titleLb.pack(pady=20, expand=True, fill=tk.BOTH)
    # the frames in which the random pattern and the setting pattern matrix will be displayed
    settingPatternFrame = tk.Frame(mainFrame)
    randomPatternFrame = tk.Frame(mainFrame)

    patternMatrix = settingGridShow(settingPatternFrame)
    randomMatrix = showRandomPattern(randomPatternFrame)

    settingPatternFrame.pack(side=tk.LEFT)
    randomPatternFrame.pack(side=tk.RIGHT)
    # button for starting to pattern match
    startBtn = tk.Button(mainFrame, bg="white", text="Trova corrispondenze", height=2)

    # result label
    risLb = tk.Label(mainFrame, bg="white", font=("Arial", 16), text="Corrispondenze trovate: 0")
    # button callback
    add_pattern_match_callback(startBtn, risLb, patternMatrix, randomMatrix, pattern_match)

    risLb.pack(pady=20, expand=True, fill=tk.BOTH)
    startBtn.pack()
    root.mainloop()
