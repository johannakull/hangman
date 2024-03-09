import random

word_list = ["automobile", "banana", "caramel"]

lives = 6

random_word = random.choice(word_list)
word_length = len(random_word)

print(random_word) # for debugging

display = []

for _ in random_word:
    display += ("_")

print("Here's your word!")
print(display)

while "_" in display and lives > 0:
    guess = input("Guess a letter: ").lower()
    
    if guess in random_word:
        for position in range(word_length):
            letter = random_word[position]
            if letter == guess:
                display[position] = guess
    else:
        lives -= 1
        if lives > 0:
            print(f"Wrong! You lost a life. You now have {lives} lives left.")
    
    print(display)

if lives == 0:
    print("You lost the game. Try again.")
else:
    print("Congratulations! You win.")
        

