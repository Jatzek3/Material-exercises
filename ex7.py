"""List Comprehensions(First method i written without problem, i had to do more reading for second)"""

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = []
for i in a:
    if i % 2 == 0:
        b.append(i)
print(b)

c = [x for x in a if x % 2 == 0]
print(c)