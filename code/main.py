import random

word_list = ["automobile", "banana", "caramel"]

random_word = random.choice(word_list)
print(random_word) # for debugging

display = []

for _ in random_word:
  display.append("_")

print("Here's your word!")
print(display)

guess = input("Guess a letter: ").lower()

word_length = len(random_word)

for position in range(word_length):
    letter = random_word[position]
    if letter == guess:
       display[position] = guess

print(display)
