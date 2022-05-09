import random
import dictionary
import scratches
from replit import clear

lives_count = len(scratches.stages)
game_over = False
chosen_word = random.choice(dictionary.word_list)
display_list = ["_"]*len(chosen_word)
print(scratches.logo)
print(f"{' '.join(display_list)}")
while not game_over:
    guessed_letter = input("Guess the letter!").lower()
    clear()
    if guessed_letter not in chosen_word:
        lives_count -= 1
        print(scratches.stages[lives_count])
        print("Wrong letter!")
        print(f"{' '.join(display_list)}")
        if lives_count == 0:
            game_over = True
            print("You lose!")
    else:
        for index, letter in enumerate(chosen_word):
            if guessed_letter == letter:
                display_list[index] = guessed_letter
        print(f"{' '.join(display_list)}")

    if "_" not in display_list:
        game_over = True
        print("You Won!")

