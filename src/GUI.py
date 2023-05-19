# in board class there is a bug as it is not possible to choose the
# index = 6 from function select_column(6) and its behavior is
# similar to select_column(0) whice will affect the win state of our
# implemented AI agent and make it always lose in hard mode
# you can check the selected columns from terminal as it is not
# our fault of implementation despite of our continuous try to debug
# the mistake as it always results in errors
import tkinter as tki
from game import minimaxGame
from game import alphaBetaGame

MINIMAX_EASY = 2
MINIMAX_MEDIUM = 4
MINIMAX_HARD = 6

ALPHABETA_EASY = 3
ALPHABETA_MEDIUM = 5
ALPHABETA_HARD = 8


def playConnect4():
    if minimaxVar.get() == checkVar.get():
        if easyVar.get() == checkVar.get():
            minimaxGame(MINIMAX_EASY)
            return
        elif mediumVar.get() == checkVar.get():
            minimaxGame(MINIMAX_MEDIUM)
            return
        elif hardVar.get() == checkVar.get():
            minimaxGame(MINIMAX_HARD)
            return
        else:
            minimaxGame(MINIMAX_EASY)
            return
    else:
        if easyVar.get() == checkVar.get():
            alphaBetaGame(ALPHABETA_EASY)
            return
        elif mediumVar.get() == checkVar.get():
            alphaBetaGame(ALPHABETA_MEDIUM)
            return
        elif hardVar.get() == checkVar.get():
            alphaBetaGame(ALPHABETA_HARD)
            return
        else:
            alphaBetaGame(ALPHABETA_EASY)
            return


root = tki.Tk()
root.geometry("600x300")
root.resizable(False, False)
root.title("Select your ALGORITHM and DIFFICULTY LEVEL")

# variables
minimaxVar = tki.IntVar()
alphaBetaVar = tki.IntVar()
easyVar = tki.IntVar()
mediumVar = tki.IntVar()
hardVar = tki.IntVar()
checkVar = tki.IntVar(value=1)

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

alphaBetaCheckBox = tki.Checkbutton(
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
