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
    root.title('Python pattern matching')

    # Frame: used to organized more elements together
    mainFrame = tk.Frame(root, highlightbackground="grey", highlightthickness=1, width=200, height=200)
    mainFrame.pack(padx=150, pady=120)

    # title lable
    titleLb = tk.Label(mainFrame, bg="white", font=("Arial", 22), text="Inserisci un pattern da cercare!", width=60, height=1, borderwidth=1, relief="ridge")
    # titleLb.pack(pady=20, expand=True, fill=tk.BOTH)
    titleLb.grid(row=0, column=0, columnspan=5)

    # the frames in which the random pattern and the setting pattern matrix will be displayed
    settingPatternFrame = tk.Frame(mainFrame, width=150, height=100)       # left
    randomPatternFrame = tk.Frame(mainFrame, width=150, height=100)        # right

    patternMatrix = settingGridShow(settingPatternFrame)
    randomMatrix = showRandomPattern(randomPatternFrame)

    settingPatternFrame.grid(row=1, column=0, padx=30, pady=30)          # select LEFT frame (setting pattern)
    randomPatternFrame.grid(row=1, column=2, padx=30, pady=30, columnspan=3)          # select RIGHT frame (random pattern)

    # button for starting to pattern match
    startBtn = tk.Button(mainFrame, bg="white", text="Trova corrispondenze", height=2)
    startBtn.grid(row=2, column=1)

    # result label
    risLb = tk.Label(mainFrame, bg="white", font=("Arial", 16), text="Corrispondenze trovate: 0")
    risLb.grid(row=1, column=1)

    # numPattern label
    numPattern = tk.Label(mainFrame, bg="white", font=("Arial", 16), text="Num pattern")
    numPattern.grid(row=2, column=3)

    # arrow
    # canvas = tk.Canvas(root)
    # canvas.create_line(20, 0, 100, 0, fill="black", arrow=tk.LAST, width=10)
    # canvas.pack(pady=20, fill=tk.BOTH, side=tk.RIGHT)

    # arrow left
    arrowButton = tk.Button(mainFrame, bg="white", text="Arrow left", height=2)
    arrowButton.grid(row=2, column=4)
    # arrow = my_canvas.create_line(70, 70, 90, 180, fill="blue", width=5)

    # arrow right
    arrowButton = tk.Button(mainFrame, bg="white", text="Arrow right", height=2)
    arrowButton.grid(row=2, column=2)

    # button callback
    add_pattern_match_callback(startBtn, risLb, patternMatrix, randomMatrix, pattern_match)

    # risLb.pack(pady=20, expand=True, fill=tk.BOTH)
    # startBtn.pack()

    root.mainloop()
