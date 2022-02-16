import os
import tkinter as tk
from random import seed
from random import randint
RAND_WIDTH = 20
RAND_HEIGTH = 20


# given a frame, it displays a random pattern in the frame
def show_random_pattern(frame):
    matr = generate_random_pattern_matr()
    for i in range(0, len(matr)):
        for j in range(0, len(matr[0])):
            if matr[i][j]:
                label = tk.Label(frame, bg="black", width=2, height=1)
            else:
                label = tk.Label(frame, bg="white", width=2, height=1, borderwidth=1, relief="raised")
            label.grid(row=i, column=j)
    return matr


def generate_random_pattern_matr():
    seed(os.getpid())
    # init matrix RAND_WIDTH x RAND_HEIGTH of random true/false
    matr = [[True if randint(0, 1) == 0 else False for x in range(RAND_WIDTH)] for y in range(RAND_HEIGTH)]
    return matr
