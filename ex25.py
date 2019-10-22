import random

F =input("Enter a number")

def guesser(x, y):
    counter = 0
    compguess =random.randint(x, y)
    print(compguess)
    user_feedback = input("Enter < in to low or > if to high")
    if int(F) == compguess:
        print(f"Correct. It took computer to solve it {counter} moves")
    if user_feedback == "<":
        guesser(compguess, y)
        counter += 1
    elif user_feedback ==">":
        guesser(x, compguess)
        counter += 1
    else:
        print("invalid input")
        guesser(x, y)


guesser(0,100)