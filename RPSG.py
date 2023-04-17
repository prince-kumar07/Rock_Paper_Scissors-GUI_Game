from tkinter import *
from random import randint
from tkinter import ttk
root = Tk()
root.title('Prince.com - Rock, Paper, Scissors')
root.iconbitmap('C:\Users\GUI')
root.geometry("500x600")

# Change bg color to white
root.config(bg="white")

# Define our images
rock = PhotoImage(file='GUI\rock.jpg')
paper = PhotoImage(file='GUI\paper.jpg')
scissors = PhotoImage(file='GUI\scissors.jpg')

# Add Images to a List
image_list = [rock, paper, scissors]

# Pick random number between 0 and 2
pick_number = randint(0,2)

# Throw up image when the program starts
image_label = Label(root, image=image_list[pick_number], bd=0)
image_label.pack(pady=20)

# Create Spin Funtion
def spin():
    # Pick random number
    pick_number = randint(0,2)
    #Show image
    image_label.config(image=image_list[pick_number])


    # 0 = Rock
    # 1 = Paper
    # 2 = Scissors


# convert Dropdown choice to a number
    if user_choise.get() == "Rock":
        user_choise_value = 0
    elif user_choise.get() == "Paper":
        user_choise_value = 1
    elif user_choise.get() == "Scissors":
        user_choise_value = 2

    # Determine if we or lost
    if user_choise_value == 0: # Rock
        if pick_number == 0:
            win_lose_label.config(text="It A Tie! Spin Agan...")
        elif pick_number == 1: # Paper
            win_lose_label.config(text="Paper Cover Rock! You Lose...")
        elif pick_number == 2: # Scissors
            win_lose_label.config(text="Rock Smashes Scissors! You Win!!!")
    

    # If User Picks Paper
    if user_choise_value == 1: # Paper
        if pick_number == 1:
            win_lose_label.config(text="It A Tie! Spin Agan...")
        elif pick_number == 0: # Rock
            win_lose_label.config(text="Paper Cover Rock! You Win!!!")
        elif pick_number == 2: # Scissors
            win_lose_label.config(text="Scissors Cuts Paper! You Lose...")


    # If User Picks Scissors
    if user_choise_value == 2: # Scissors
        if pick_number == 2:
            win_lose_label.config(text="It A Tie! Spin Agan...")
        elif pick_number == 0: # Rock
            win_lose_label.config(text="Rock Smashes Scissors! You Lose...")
        elif pick_number == 1: # Paper
            win_lose_label.config(text="Scissors Cuts Paper! You Win!!!")


# Make our choice
user_choise = ttk.Combobox(root, value=("Rock", "Paper", "Scissors"))
user_choise,CURRENT(0)
user_choise.pack(paddy=20)
# Create Spin Button
spin_button = Button(root, text="Spin!", command=spin)
spin_button.pack(pady=10)


#Label for showing if you won or not
win_lose_label = Label(root, text="", font=("Helvetica",18), bg="white")
win_lose_label.pack(pady=50)

root.mainloop()
