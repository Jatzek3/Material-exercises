
x = open("names", 'r')
y = x.readlines()


for i in y:
    print(y.count(i))

x.close()

