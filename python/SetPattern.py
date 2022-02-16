import tkinter as tk

WIDTH = 3
HEIGHT = 3

# init matrix WIDTH x HEIGTH of all false
patternMatrix = [[False for x in range(WIDTH)] for y in range(HEIGHT)]


# required since default tkinter does not provide argument for callback function
def add_callback(control, i, j, fun):
    def inner():
        return fun(control, i, j)

    control['command'] = inner


def flip(button, i, j):
    patternMatrix[i][j] = not patternMatrix[i][j]
    if patternMatrix[i][j]:
        button["bg"] = "black"
    else:
        button["bg"] = "white"


# given a frame, it displays the setting grid in the frame
def settingGridShow(frame):
    for i in range(0, WIDTH):
        for j in range(0, HEIGHT):
            button = tk.Button(frame, bg="white", width=5, height=2)
            add_callback(button, i, j, flip)
            button.grid(row=i, column=j)
    return patternMatrix
