#Python Hangman

from __future__ import print_function
import numpy

#These are variables I am setting now to use later
num_correct = 0
num_wrong = 0

#This is my word list
words = ["sky", "shy", "jazz", "wall", "glee", "why", "cry", "yush", "rye", "bye", "sly", "spy", "fry", "try", "zest", "pez", "job", "bob"]

#This selects a random word from the list then counts how many letters are in the word
word = numpy.random.choice(words)
spaces = len(word)

#This identifies how many times you have guessed wrong and prints the corresponding picture
def picture():
    if num_wrong == 0:
        print("__________")
        print("[         ]")
        print("[")
        print("[")
        print("[")
        print("[")
        print("------------")
    elif num_wrong == 1:
        print("__________")
        print("[         ]")
        print("[         O")
        print("[")
        print("[")
        print("[")
        print("------------")
    elif num_wrong == 2:
        print("__________")
        print("[         ]")
        print("[         O")
        print("[         [")
        print("[         [")
        print("[")
        print("------------")
    elif num_wrong == 3:
        print("__________")
        print("[         ]")
        print("[         O")
        print("[        \[")
        print("[         [")
        print("[")
        print("------------")
    elif num_wrong == 4:
        print("__________")
        print("[         ]")
        print("[         O")
        print("[        \[/")
        print("[         [")
        print("[")
        print("------------")
    elif num_wrong == 5:
        print("__________")
        print("[         ]")
        print("[         O")
        print("[        \[/")
        print("[         [")
        print("[        /")
        print("------------")

#This prints the initial hangman
print("__________")
print("[         ]")
print("[")
print("[")
print("[")
print("[")
print("------------")

print("_ " * spaces)

correct_letters = []
solved = False

while True:
    if solved:
        print("YOU WON!")
        print("The word was " + word)
        break
    elif num_wrong == 6:
        print("YOU  LOST!")
        print("The word was " + word)
        break
    else:
        letter = raw_input("What is your guess?")
        if letter in word:
            print("correct")
            correct_letters.append(letter)
            letter = ' '
            num_correct += 1
            picture()
        elif letter not in word:
            print("wrong")
            letter = ' '
            num_wrong += 1
            picture()
        solved = True
        for letter in word:
            if letter in correct_letters:
                print(letter + " ", end = "")
            else:
                print("_ ", end = "")
                solved = False
        print("")