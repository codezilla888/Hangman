import random

stages = ['''
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
=========''', '''
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
''']

lives_count = len(stages)
word_list = ["ardvark", "baboon", "camel"]
game_over = False
chosen_word = random.choice(word_list)
display_list = ["_"]*len(chosen_word)
print(display_list)
while not game_over:
    guessed_letter = input("Guess the letter!").lower()
    if guessed_letter not in chosen_word:
        lives_count -= 1
        print(stages[lives_count])
        print("Wrong letter!")
        if lives_count == 0:
            game_over = True
            print("You lose!")
    else:
        for index, letter in enumerate(chosen_word):
            if guessed_letter == letter:
                display_list[index] = guessed_letter
        print(display_list)

    if "_" not in display_list:
        game_over = True
        print("You Won!")

