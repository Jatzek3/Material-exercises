import random


with open("sowpods.txt", "r") as file:
    words = file.readlines()

randWord = random.choice(words)
print(randWord)