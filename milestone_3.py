while True:
            guess = input("Please guess a letter: ").lower()
            
            if guess.isalpha():
                   break
                
                           
            else:
                print("Invalid letter. Please, enter a single alphabetical character.")