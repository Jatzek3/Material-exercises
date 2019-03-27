"""Check Primality Functions. (wrote a function which checks for divisors and checks the boolean for list."""

number = int(input("give me a number"))
list =[]

for i in range(2, number):
    if number % i == 0:
        list.append(i)

if bool(list) == False:
    print("It is a prime number")
else:
    print("It isn't a prime number")
print(list)
