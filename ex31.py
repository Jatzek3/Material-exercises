
def guessing(ABC):
    hidden = ABC.upper()
    unguessedWord =[]
    counter = 0
    for i in hidden:
        unguessedWord.append("_")

    while True:
        guess = input("Guess your letter")
        guess = guess.upper()
        for guess in hidden:
            unguessedWord[hidden.index(guess)] = guess
            print(unguessedWord)
            counter += 1
        else:
            print(unguessedWord)
            counter += 1
        check = "".join(unguessedWord)
        if check.isalpha():
            print(f"You have won in {counter} moves")

