import random

ordered_list = [1,2,3,4,5,6,7,8,9]
number = random.randint(0, 15)

def checking(list, number):
    if number in list:
        print(True)
        return True
    else:
        print(False)
        return False

if __name__ == '__main__':
    checking(ordered_list, number)
