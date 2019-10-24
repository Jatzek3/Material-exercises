def maxlist(x,y,z):
    list = [x,y,z]
    newlist = sorted(list)
    print(newlist)
    return newlist[-1]

maxlist(1,6,3)