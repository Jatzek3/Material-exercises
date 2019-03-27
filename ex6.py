"""A string is a List(had some problems with this one, didn't knew how exactly i should use indexing and tried to
create a list of a second string)"""

string1 = input("Give your string")
if string1[::-1] == string1:
    print("is a palindrome")
else:
    print("is not a Palindrome")
