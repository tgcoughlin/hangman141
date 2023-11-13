word = "apple"


def check_guess(guess):
    
    if guess.lower() in word:
            print(f"Good guess, the letter {guess} is in the word!")
    else:
            print(f"Sorry, {guess} is not in the word. Try again.")



def ask_for_input():
    while True:
                guess = input("Please guess a letter: ")
                
                if guess.isalpha():
                    check_guess(guess)
                    return guess
                    
                            
                else:
                    print("Invalid letter. Please, enter a single alphabetical character.")
    
    

ask_for_input()



