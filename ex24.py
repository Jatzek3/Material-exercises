def makeBoard(matrix=3):
    for i in range(matrix):
        print((" ___ ") * (matrix))
        print(("|    ") * (matrix + 1))
    print((" ___ ") * matrix)

makeBoard()