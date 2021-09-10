import os

os.chdir("/Users/tim10/Desktop/Python Files/Project euler")

file = open('Problem 13.txt', 'r')

a = file.read()
b = []

b.append(a)

c = ''.join(b)
d = c.replace('\n', '+')

print(eval(d))