import random
stages = [
    '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
'''
]
lives = 6
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
 

placeholder = "_" * len(chosen_word)
print(placeholder)

correct_letters = []
game_over = False

while not game_over:
    guess = input("Guess a letter: ").lower()
    
    new_display = ""

    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            new_display += guess
            correct_letters.append(guess)
    
        else:
            new_display += placeholder[i]

    if guess not in chosen_word and guess not in correct_letters:
        lives -= 1
        if lives == 0:
            game_over = True
            print("***************************************you lose !************************************")

    

    placeholder = new_display
    print(placeholder)

    if "_" not in placeholder:
        game_over = True
        print("*************************************You win!!*********************************************")
    print(stages[lives])
