from tkinter import *
import random
from PIL import ImageTk, Image

root = Tk()

root.title("Number Guessing Game")

# Window_size
root.geometry("600x600")
root.config(bg="#F9CFF2")

# image open
image = Image.open("img_4.png")  # make sure the image exists in same folder
resized = image.resize((230, 225))
photo = ImageTk.PhotoImage(resized)
image_label = Label(root, image=photo, bg="#D59FBE")
image_label.pack(pady=(10, 0))


# game variables
rand_number = random.randint(0, 100)
chances = 3
var = IntVar()
display = StringVar()


def checkguessnumber():
    global rand_number
    global chances

    userinput = var.get()

    if chances > 0:
        if userinput == rand_number:
            msg = f"🎉 Congratulations! {userinput} is the right answer"
        elif userinput < rand_number:
            chances -= 1
            msg = f"⬇️ Too low! You have {chances} chances left."
        elif userinput > rand_number:
            chances -= 1
            msg = f"⬆️ Too high! You have {chances} chances left."
        else:
            msg = "Something went wrong, sorry :("
    else:
        msg = f"❌ No chances left! The number was {rand_number}\nClick 'NEW GAME' to play again!"

    display.set(msg)

def new_game():
    global rand_number
    global chances
    rand_number = random.randint(0, 100)
    chances = 5
    var.set(0)
    display.set("🔄New game started! Guess the number between 0 and 100.")

head1 = Label(root, text="Welcome to the Number Guessing Game",
              font=("Times New Roman", 19, "bold"), relief=SOLID,
              bg="#DAE0F2", fg="black", padx=10, pady=10)
head1.pack(pady=(5, 0))

head2 = Label(root,text="I am thinking of a number between 0 and 100, You can start guessing!",font=("Times New Roman", 15), relief=SOLID,bg="#F1C4B5", fg="black", padx=5, pady=10)
head2.pack(pady=(10, 0))

# user entry
entry = Entry(root, textvariable=var, font=("Times New Roman", 18))
entry.pack(pady=10)

# submit-button
submit_bt = Button(root, fg="black", text="SUBMIT ANSWER!", command=checkguessnumber, padx=10, pady=10)
submit_bt.pack(pady=5)

#submit button
result_label = Label(root, textvariable=display, font=("Times New Roman", 14), bg="#D59FBE")
result_label.pack(side=TOP, pady=10)

# New Game button
newgamebt = Button(root, fg="black", text="NEW GAME!", command=new_game, padx=10, pady=10)
newgamebt.pack(pady=5)

# quit button
quitgame = Button(root, fg="black", text="QUIT", command=root.quit, padx=10, pady=10)
quitgame.pack(pady=5)

# start first game message
new_game()

root.mainloop()
