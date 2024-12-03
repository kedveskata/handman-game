import random
from string import ascii_uppercase
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Python Hangman")

# Color
text_color = '#3b7ac4'

# Lists
word_list = ["key", "Mutable", "dIcTiOnArY", "set", "FROZENSET", "tuple", "unpacking", "ARGS", "KWARGS", "Lambda",
             "sorting", "functools", "cLoSuRe", "decorator", "Fibonacci", "class", "TKINTER", "ascii", "Python"]

hangman = ["+---+\n    |\n    |\n    |\n   ===", "+---+\nO  |\n    |\n    |\n   ===", "+---+\nO  |\n|   |\n    |\n   ===",
		   "+---+\nO  |\n/|  |\n    |\n   ===", "+---+\nO  |\n/|\ |\n    |\n   ===", "+---+\nO  |\n/|\ |\n/   |\n   ===",
           "+---+\nO  |\n/|\ |\n/\  |\n   ==="]

#Word label
guess_word = StringVar()

# Functions
def new_game():
    global word_with_spaces
    global number_of_wrong_guesses
    global random_word
    number_of_wrong_guesses = 0


    random_word = random.choice(word_list)
    word_with_spaces = " ".join(random_word)
    guess_word.set(' '.join("_" * len(random_word)))
    hangman_Label.config(text=hangman[0])

won = 0
lost = 0

def guess(char):
    global number_of_wrong_guesses
    global won
    global lost

    if number_of_wrong_guesses < 6:
        word = list(word_with_spaces.upper())
        guessed = list(guess_word.get())

        if word_with_spaces.upper().count(char) > 0:
            for c in range(len(word)):
                if word[c] == char:
                    guessed[c] = char
                guess_word.set("".join(guessed))

            if guess_word.get() == word_with_spaces.upper():
                won += 1
                messagebox.showinfo("｡ﾟ( ﾟ^∀^ﾟ)ﾟ｡", f'Good Job!\nWon: {won} Lost: {lost}')
        else:
            number_of_wrong_guesses += 1
            hangman_Label.config(text=hangman[number_of_wrong_guesses])

            if number_of_wrong_guesses == 6:
                lost += 1
                messagebox.showwarning("(`皿´＃)", f'Better luck next time!\n\nThe word was: {random_word}\n\nWon: {won} Lost: {lost}')


# Layout
# guess_word label
Label(root, textvariable=guess_word, fg=text_color, font='Verdena 24 bold').grid(row=0, column=3, columnspan=6, padx=10)

hangman_Label = Label(root, fg=text_color, font='Verdena 24 bold')
hangman_Label.grid(row=0, column=0, columnspan=3, padx=10, pady=40)

# Input
n = 0
for char in ascii_uppercase:
    Button(root, text=char, command=lambda c=char: guess(c), fg=text_color, font='Verdena 16', width=4).grid(row=1 + n // 9, column=n % 9)
    n += 1

Button(root, text="New\nGame", command=lambda: new_game(), bg=text_color, fg='#fff', font="Verdena 10 bold").grid(row=3, column=8)


messagebox.showinfo("(｡･ω･)ﾉﾞ Hello♪", "Try to guess the word!\n\nTip:  The word was mentioned during the Advanced Python Programming course.")
new_game()
root.mainloop()
