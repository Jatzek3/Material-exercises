with open('happynumbers.txt', 'r') as happy:
    happyN = happy.readlines()

with open('primenumbers.txt', 'r') as prime:
    primeN =prime.readlines()

print(type(happyN), type(primeN))


def converter(list):
    new_list =[]
    for i in list:
        if "\n" in i:
            i.strip()
            i = int(i)
            new_list.append(i)
    return new_list

x = converter(happyN)
y = converter(primeN)

x = set(x)
y = set(y)

intersection = x & y
print(intersection)



