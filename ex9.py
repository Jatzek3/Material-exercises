""" Guessing game.(Had some problems with while loop, and decided to set a variable guessed)"""
import random


number = random.randint(0, 9)

guessnumber = 1  # because of first attempt which isn't counted

guessed = False

while guessed == False:
    guess = int(input("Give a number from 0 to 9"))
    if guess == number:
        guessed = True
        print("you have guest congratulations!")
        print(f"It took you {guessnumber} attemps")
    else:
        guessnumber += 1
        print("try again")
