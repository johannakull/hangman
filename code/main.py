import random

word_list = ["automobile", "banana", "caramel"]
random_word = random.choice(word_list).upper()
word_length = len(random_word)

lives = 6

display = []

print("WELCOME TO HANGMAN\n")
print("Try to guess the following word! You have 6 lives.\n")

for _ in random_word:
    display += ("_")

print(*display, sep=" ")
print()

while "_" in display and lives > 0:
    guess = input("\nGuess a letter: ").upper()
    
    if guess in random_word:
        for position in range(word_length):
            letter = random_word[position]
            if letter == guess:
                display[position] = guess
        print("\nCorrect!\n")
    else:
        lives -= 1
        if lives > 1:
            print(f"\nSorry, {guess} is incorrect - you lose a life. You now have {lives} lives left.\n")
        elif lives == 1:
            print(f"\nSorry, {guess} is incorrect - you lose a life. You now have {lives} life left.\n")
        else:
            print()
    
    print(*display, sep=" ")

if lives == 0:
    print("\nYou lost the game. Try again.")
else:
    print("\nCongratulations! You win.")
        

