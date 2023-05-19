import tkinter as tki
from game import minimaxGame
from game import alphaBetaGame

EASY = 2
MEDIUM = 5
HARD = 7


def playConnect4():
    if minimaxVar == 1:
        if easyVar == 1:
            minimaxGame(EASY)
        if mediumVar == 1:
            minimaxGame(MEDIUM)
        if hardVar == 1:
            minimaxGame(HARD)
    if alphaBetaVar == 1:
        if easyVar == 1:
            alphaBetaGame(EASY)
        if mediumVar == 1:
            alphaBetaGame(MEDIUM)
        if hardVar == 1:
            alphaBetaGame(HARD)


root = tki.Tk()
root.geometry("500x300")
root.resizable(False, False)
root.title("Select your ALGORITHM and DIFFICULTY LEVEL")

# variables
minimaxVar = tki.IntVar()
alphaBetaVar = tki.IntVar()
easyVar = tki.IntVar()
mediumVar = tki.IntVar()
hardVar = tki.IntVar()

lab = tki.Label(
    root,
    text="Select the algorithm type",
    bg="#1f2f54",
    fg="white",
    width=20,
    height=2,
).pack()


minimaxCheckBox = tki.Checkbutton(
    root,
    text="Minimax",
    variable=minimaxVar,
    onvalue=1,
    offvalue=0,
).pack()

minimaxCheckBox = tki.Checkbutton(
    root,
    text="Alpha-Beta",
    variable=alphaBetaVar,
    onvalue=1,
    offvalue=0,
).pack()

lab2 = tki.Label(
    root,
    text="Difficulty level of the game",
    bg="#1f2f54",
    fg="white",
    width=20,
    height=2,
).pack()

easyCheckBox = tki.Checkbutton(
    root,
    text="EASY",
    variable=easyVar,
    onvalue=1,
    offvalue=0,
).pack()

mediumCheckBox = tki.Checkbutton(
    root,
    text="MEDIUM",
    variable=mediumVar,
    onvalue=1,
    offvalue=0,
).pack()

hardCheckBox = tki.Checkbutton(
    root,
    text="HARD",
    variable=hardVar,
    onvalue=1,
    offvalue=0,
).pack()

playButton = tki.Button(
    root,
    text="Play",
    bg="#1f2f54",
    fg="white",
    width=15,
    height=2,
    command=playConnect4,
).pack()


root.mainloop()
