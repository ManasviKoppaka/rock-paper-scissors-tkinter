from tkinter import *
from random import choice
root = Tk()
root.title("Rock, Paper, Scissors")
root.geometry("350x500")


playerScore=0
compScore=0


label1 = Label(text="Computer's Choice", bg="white", fg="black", height=2, width=15, borderwidth=5, relief=SUNKEN)
label1.grid(row=0, column=4)
label2 = Label(text="Player", bg="white", fg="black", height=2, width=15, borderwidth=5, relief=SUNKEN)
label2.grid(row=0,column=0)
label4=Label(text="Winner!", bg="white", fg="black", height=2, width=15, borderwidth=5, relief=SUNKEN)
label4.grid(row=0, column=3)
label3 = Label(text="Score", bg="white", fg="black", height=2, width=10, borderwidth=5, relief=RAISED)
label3.grid(row=5, column=3)
label5 = Label(text=playerScore, bg="white", fg="black", height=2, width=10, borderwidth=5, relief=SUNKEN)
label5.grid(row=4, column=0)
label6 = Label(text=compScore, bg="white", fg="black", height=2, width=10, borderwidth=5, relief=SUNKEN)
label6.grid(row=4, column=4)

def checkWinner(user, comp):
    global playerScore
    global compScore
    if user == comp:
        draw["bg"]="yellow"
        draw["fg"]="black"
        return "draw"
    if user == "rock":
        if comp == "paper":
            compScore+=1
            compWin["bg"]="yellow"
            compWin["fg"]="black"
            return  "computer"
        else:
            playerScore+=1
            playerWin["bg"]="yellow"
            playerWin["fg"]="black"
            return "player"
    elif user == "paper":
        if comp == "rock":
            playerScore+=1
            playerWin["bg"]="yellow"
            playerWin["fg"]="black"
            return "player"
        else:
            compScore+=1
            compWin["bg"]="yellow"
            compWin["fg"]="black"
            return "computer"
    else:
        if comp == "rock":
            compScore+=1
            compWin["bg"]="yellow"
            compWin["fg"]="black"
            return "computer"
        else:
            playerScore+=1
            playerWin["bg"]="yellow"
            playerWin["fg"]="black"
            return "player"



def reset():
    global playerScore
    global compScore

    rockButton["bg"]="black"
    rockButton["fg"]="white"

    paperButton["bg"]="black"
    paperButton["fg"]="white"

    scissorButton["bg"]="black"
    scissorButton["fg"]="white"



    rockButtonComp["bg"]="black"
    rockButtonComp["fg"]="white"

    paperButtonComp["bg"]="black"
    paperButtonComp["fg"]="white"

    scissorButtonComp["bg"]="black"
    scissorButtonComp["fg"]="white"

    draw["bg"]="black"
    draw["fg"]="white"

    playerWin["bg"]="black"
    playerWin["fg"]="white"

    compWin["bg"]="black"
    compWin["fg"]="white"

def updateResult():
    if compScore==10 and compScore>playerScore:
        label7=Label(text="Computer is the winner!", bg="black", fg="white", font=("arial narrow", 6), height=2, width=20, borderwidth=5, relief=SUNKEN)
        label7.grid(row=8, column=3)
    elif playerScore==10 and playerScore>compScore:
        label8=Label(text="Player is the winner!", bg="black", fg="white", font=("arial narrow", 10), height=2, width=20, borderwidth=5, relief=SUNKEN)
        label8.grid(row=8, column=3)
    else:
        label8=Label(text="----------", bg="black", fg="white", font=("arial narrow", 10), height=2, width=10, borderwidth=5, relief=SUNKEN)
        label8.grid(row=8, column=3)

def fullRestart():
    global playerScore
    global compScore

    playerScore=0
    compScore=0

    reset()
    updateScore()
    updateResult()


def updateScore():
    label5 = Label(text=playerScore, bg="white", fg="black", height=2, width=10, borderwidth=5, relief=SUNKEN)
    label5.grid(row=4, column=0)
    label6 = Label(text=compScore, bg="white", fg="black", height=2, width=10, borderwidth=5, relief=SUNKEN)
    label6.grid(row=4, column=4)


def play(user):
    reset()
    if user == "rock":
        rockButton["bg"]="yellow"
        rockButton["fg"]="black"
    elif user == "paper":
        paperButton["bg"]="yellow"
        paperButton["fg"]="black"
    elif user == "scissor":
        scissorButton["bg"]="yellow"
        scissorButton["fg"]="black"

    game = "rock", "paper", "scissor"
    comp = choice(game)
    if comp == "rock":
        rockButtonComp["bg"]="yellow"
        rockButtonComp["fg"]="black"
    elif comp == "paper":
        paperButtonComp["bg"]="yellow"
        paperButtonComp["fg"]="black"
    elif comp == "scissor":
        scissorButtonComp["bg"]="yellow"
        scissorButtonComp["fg"]="black"

    checkWinner(user,comp)
    updateScore()
    updateResult()





rockButton = Button(text="Rock", command=lambda:play("rock"), bg="black", fg="white", relief=RAISED, borderwidth=5, width=10)
rockButton.grid(row=1,column=0)

paperButton = Button(text="Paper", command=lambda:play("paper"), bg="black", fg="white", relief=RAISED, borderwidth=5, width=10)
paperButton.grid(row=2, column=0)

scissorButton = Button(text="Scissors", command=lambda:play("scissor"), bg="black", fg="white", relief=RAISED, borderwidth=5, width=10)
scissorButton.grid(row=3, column=0)



rockButtonComp = Button(text="Rock", command=play, bg="black", fg="white", relief=RAISED, borderwidth=5, width=10)
rockButtonComp.grid(row=1,column=4)

paperButtonComp = Button(text="Paper", command=play, bg="black", fg="white", relief=RAISED, borderwidth=5, width=10)
paperButtonComp.grid(row=2, column=4)

scissorButtonComp = Button(text="Scissors", command=play, bg="black", fg="white", relief=RAISED, borderwidth=5, width=10)
scissorButtonComp.grid(row=3, column=4)





playerWin = Button(text="Player", command=play, bg="black", fg="white", relief=RAISED, borderwidth=5, width=10)
playerWin.grid(row=1,column=3)

compWin = Button(text="Computer", command=play, bg="black", fg="white", relief=RAISED, borderwidth=5, width=10)
compWin.grid(row=2, column=3)

draw = Button(text="Draw", command=play, bg="black", fg="white", relief=RAISED, borderwidth=5, width=10)
draw.grid(row=3, column=3)

restart = Button(text="Restart", command=fullRestart, bg="black", fg="white", relief= RAISED, borderwidth=5, width=10)
restart.grid(row=7, column=3)

root.mainloop()