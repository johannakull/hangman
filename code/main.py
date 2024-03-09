import random

word_list = ["automobile", "banana", "caramel"]

random_word = random.choice(word_list)
print(random_word)

display = []

for letter in random_word:
  display.append("_")

print("Here's your word!")
print(display)

guess = input("Guess a letter: ").lower()

letter_index = 0

for letter in random_word:
    if letter == guess:
        display[letter_index] = letter
    letter_index += 1

print(display)
