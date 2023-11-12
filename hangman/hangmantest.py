list_letters = []
        
while len(letter) != 1 or letter in list_letters:
  print("Please guess a letter for the secret word: ")
  letter = input()
        
  if len(letter) != 1:
    print("Please, enter just one character:")
    letter = input()
  elif letter in list_letters:
    print(f"{letter} has already been tried")
    letter = input()
  else:
    list_letters.append(letter)