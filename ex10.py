"""List Overlap Comprehensions (Very easy since ive done list comprehensions today. Didnt knew the sample method)"""
import random



a = random.sample(range(100), 30)
b = random.sample(range(100), 40)

c = [x for x in a if x in b]
print(set(c))
