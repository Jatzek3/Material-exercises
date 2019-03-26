number = int(input("Please insert a number"))
if number % 4 == 0:
    print("Your number is divisable by 4")
elif number % 2 == 0:
    print("your number is even")
else:
    print("Your number is odd")

first = int(input("Give me first"))
second = int(input("Give me second"))
if first % second == 0:
    print("You can divide")
else:
    print("You cannot divide")