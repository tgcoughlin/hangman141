import random

word_list = ["apple", "grapes", "peach", "banana", "pear"]

word = random.choice(word_list)

print(word)

guess = input("Please enter your guess, this should be a single letter of the alphabet: ")
if len(guess) == 1 and guess.isalpha():
    print ("Good guess!")
else:
    print("Oops! That is not a valid input.")
    





