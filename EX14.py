"""List Remove Duplicates(Part using sets was very easy, the one for iteration was very tough for me)"""
import random

a = random.sample(range(10), 4)
b = random.sample(range(10), 9)
list = a + b
print(list)


def uncommon_iteration(x):
    uncommon1 = []
    for i in x:
        if i not in uncommon1:
            uncommon1.append(i)
    print(uncommon1)
    return uncommon1


uncommon_iteration(list)

def uncomon_set(x):
    uncomon2 = set(list)
    print(uncomon2)
    return uncomon2

uncomon_set(list)

