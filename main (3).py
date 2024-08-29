from replit import clear
import random
import hangman_art
from rainbow import rainbowInit, rainbowText, rainbowBlock
from time import sleep
import os

rainbowInit(os)

sleep(0.5)
# for logo
print(rainbowText(hangman_art.logo))
# for word
import hangman_words
chosen_word = random.choice(hangman_words.word_list)
# for postion of word
word_length = len(chosen_word)
# for cotinuing loop
end_of_game = False
lives = 6
# for generating "_" for word
display = []
for _ in range(word_length):
    display += "_"
# for cotinuing loop  
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word: 
        lives -= 1
        print(f"you guessed {guess} , that's not in word. You have {lives} lives remaining")
        if lives == 0:
            end_of_game = True
            print(f"You lose.your word was{chosen_word}")
    print(f"{' '.join(display)}") 
    if "_" not in display:
        end_of_game = True
        print("You win.")

   
    print(rainbowText(hangman_art.stages[lives]))