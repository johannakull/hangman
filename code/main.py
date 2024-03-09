import random

word_list = ["automobile", "banana", "caramel"]

random_word = random.choice(word_list)
word_length = len(random_word)

print(random_word) # for debugging

display = []

for _ in random_word:
    display += ("_")

print("Here's your word!")
print(display)

while "_" in display:
    guess = input("Guess a letter: ").lower()
    
    for position in range(word_length):
        letter = random_word[position]
        if letter == guess:
            display[position] = guess
    
    print(display)
        

