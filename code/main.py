import random
import hangman_words
import hangman_art

random_word = random.choice(hangman_words.word_list).upper()
word_length = len(random_word)

lives = 7

display = []
guessed_letters = []

print("\nWELCOME TO HANGMAN\n")
print(f"Try to guess the word! You have {lives} lives.\n")

for _ in random_word:
    display += ("_")

print(*display, sep=" ")
print()

while "_" in display and lives > 0:
    guess = input("\nGuess a letter: ").upper() # TO DO: handle user entering multiple letters

    if guess in guessed_letters:
        print(f"You already guessed the letter {guess}. Try a different one.")
    else:
        guessed_letters.append(guess)

        if guess in random_word:
            for position in range(word_length):
                letter = random_word[position]
                if letter == guess:
                    display[position] = guess
            print("Correct!\n")
            print(*display, sep=" ")
        else:
            lives -= 1
            if lives > 1:
                print(f"Sorry, {guess} is incorrect - you lose a life. You now have {lives} lives left.\n")
            elif lives == 1:
                print(f"Sorry, {guess} is incorrect - you lose a life. You now have {lives} life left.\n")
            else:
                print(f"Sorry, {guess} is incorrect.\n")

            print(*display, sep=" ")
            print(hangman_art.stages[lives])
    
if lives == 0:
    print(f"You lost all your lives - Game Over!\nThe word was {random_word}.")
else:
    print("Congratulations! You win.")
        