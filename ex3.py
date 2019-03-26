a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
anew =[]
bigger = int(input("give me a number"))
for i in a:
    if i < bigger:
        anew.append(i)
print(anew)