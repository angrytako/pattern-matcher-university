import tkinter as tk

from PIL import ImageTk

from ShowRandPattern import *
from SetPattern import *
countPatternFounded = 1
totPatternFounded = 5      # es. 5 --> da mettere il num totali trovato


# to be used in order to add the pattern_match as a callback to the button
def add_pattern_match_callback(numPatternLb, control, risLb, patternMatr, mainMatr, fun):
    def inner():
        if totPatternFounded > 0:
            numPatternLb.config(text="Num pattern : " + str(countPatternFounded) + "/" + str(totPatternFounded))
        return fun(risLb, patternMatr, mainMatr)

    control['command'] = inner


# still has to be implemented
def pattern_match(label, patternMatr, mainMatr):
    print(patternMatr)
    pass


def next_image_callback(control, label):
    def inner():
        global countPatternFounded
        if totPatternFounded > 0:
            if countPatternFounded < totPatternFounded:
                countPatternFounded = countPatternFounded + 1
            return label.config(text="Num pattern : " + str(countPatternFounded) + "/" + str(totPatternFounded))

    control['command'] = inner


def prev_image_callback(control, label):
    def inner():
        global countPatternFounded
        if totPatternFounded > 0:
            if countPatternFounded > 1:
                countPatternFounded = countPatternFounded - 1
            return label.config(text="Num pattern : " + str(countPatternFounded) + "/" + str(totPatternFounded))

    control['command'] = inner


if __name__ == "__main__":
    root = tk.Tk()
    root.title('Python pattern matching')

    # background pic
    backgroundImage = tk.PhotoImage(file=r"python/scr/img/background.png")
    # backgroundImage = backgroundImage.subsample(2, 1)
    label = tk.Label(root, image=backgroundImage)
    label.place(x=0, y=0)

    # Frame: used to organized more elements together
    mainFrame = tk.Frame(root, highlightbackground="grey", highlightthickness=1, width=200, height=200)
    mainFrame.pack(padx=150, pady=120)

    # title lable
    titleLb = tk.Label(mainFrame, bg="white", font=("Arial", 22), text="Inserisci un pattern da cercare!", width=60,
                       height=1, borderwidth=1, relief="ridge")
    # titleLb.pack(pady=20, expand=True, fill=tk.BOTH)
    titleLb.grid(row=0, column=0, columnspan=5)

    # the frames in which the random pattern and the setting pattern matrix will be displayed
    settingPatternFrame = tk.Frame(mainFrame, width=150, height=100)  # left
    randomPatternFrame = tk.Frame(mainFrame, width=150, height=100)  # right

    patternMatrix = settingGridShow(settingPatternFrame)
    randomMatrix = showRandomPattern(randomPatternFrame)

    settingPatternFrame.grid(row=1, column=0, padx=30, pady=30)  # select LEFT frame (setting pattern)
    randomPatternFrame.grid(row=1, column=2, padx=30, pady=30, columnspan=3)  # select RIGHT frame (random pattern)

    # button for starting to pattern match
    startBtn = tk.Button(mainFrame, bg="white", text="Trova corrispondenze", height=2)
    startBtn.grid(row=2, column=1)

    # result label
    risLb = tk.Label(mainFrame, bg="white", font=("Arial", 16), text="Corrispondenze trovate: 0")
    risLb.grid(row=1, column=1)

    # numPattern label
    numPatternLb = tk.Label(mainFrame, bg="white", font=("Arial", 16), text="Num pattern : 0")
    numPatternLb.grid(row=2, column=3)

    # arrow left with image
    picLeft = tk.PhotoImage(file=r"python/scr/img/arrow_left.png")
    arrowLeftButton = tk.Button(mainFrame, bg="white", text="Arrow left", image=picLeft, width=60, height=30)
    arrowLeftButton.grid(row=2, column=2)
    # arrow = my_canvas.create_line(70, 70, 90, 180, fill="blue", width=5)

    # arrow right with image
    picRight = tk.PhotoImage(file=r"python/scr/img/arrow_right.png")
    arrowRightButton = tk.Button(mainFrame, bg="white", text="Arrow right", image=picRight, width=60, height=30)
    arrowRightButton.grid(row=2, column=4)

    # button callback
    add_pattern_match_callback(numPatternLb, startBtn, risLb, patternMatrix, randomMatrix, pattern_match)

    # next image
    next_image_callback(arrowRightButton, numPatternLb)

    # prev image
    prev_image_callback(arrowLeftButton, numPatternLb)

    # risLb.pack(pady=20, expand=True, fill=tk.BOTH)
    # startBtn.pack()

    root.mainloop()
