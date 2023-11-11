import random

word_list = ["apple", "grapes", "peach", "banana", "pear"]

word = random.choice(word_list)

print(word)

print("Please enter your guessed letter: ")
guess = input()
if len(guess) == 1 and type(guess) == str:
    print ("Good guess!")
else:
    print("Oops! That is not a valid input.")
    





