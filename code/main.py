import random

word_list = ["automobile", "banana", "caramel"]

chosen_word = random.choice(word_list)
print(chosen_word)

display = []
for letter in chosen_word:
  display.append("_")

print(display)

guess = input("Guess a letter: ").lower()

for letter in chosen_word:
    if letter == guess:
        print("yes")
    else:
        print("no")
