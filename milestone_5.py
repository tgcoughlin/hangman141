import random

class Hangman:

    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word_list)
        self.word_guessed = ["_" for _ in self.word]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []
    

    def check_guess(self, guess):
        if guess.lower() in self.word:
            print(f"Good guess! {guess} is in the word.")
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    self.word_guessed[i] = guess

            self.num_letters -= 1 
            print(self.word_guessed) 
            
        else:
            print(f"Sorry {guess} is not in the word")
            self.num_lives -= 1
            print(f"You have {self.num_lives} lives remaining")



    def ask_for_input(self):
        while True:
            guess = input("Please guess a letter: ")
                
            if not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
                    
                            
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                return guess 



def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    
    while True:
        if game.num_lives == 0:
            print(f"GAME OVER! The answer was {game.word}")
            break
        
        elif game.num_letters > 0:
             game.ask_for_input()
                     
        else:
            if game.num_lives > 0 and game.num_letters == 0:
                print(f"Congratulations you won the game! The answer was {game.word}")
                break    





word_list = ["car", "bike", "aeroplane", "train"]

play_game(word_list)



