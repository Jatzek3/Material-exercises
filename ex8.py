"""Rock paper scissors game(took me a while before i reflected that i should be using upper instead of lower:D)"""

while True:
    player1 = input("Choose (R)ock, (P)aper or (S)cissors")
    player2 = input("Choose (R)ock, (P)aper or (S)cissors")
    player1 = player1.upper()
    player2 = player2.upper()

    if player1 == player2:
        print("choose 1 more time")
    elif player1 == "R" and player2 == "S":
        print("player 1 wins")
    elif player1 == "P" and player2 == "R":
        print("player 1 wins")
    elif player1 == "S" and player2 == "P":
        print("player 1 wins")
    elif player2 == "P" and player1 == "R":
        print("player 2 wins")
    elif player2 == "R" and player1 == "S":
        print("player 2 wins")
    elif player2 == "S" and player1 == "P":
        print("player 2 wins")
    else:
        break
