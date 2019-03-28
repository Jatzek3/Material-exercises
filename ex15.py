"""Reverse Word Order(heh, that one was easy, another one solved in 5 min)"""

long_string = input("Please write something long (which is composed of words)")

list = long_string.split(" ")
print(list)

reverse = []

for i in list[::-1]:
    reverse.append(i)

print(reverse)