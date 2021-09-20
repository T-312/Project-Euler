file = open('Problem 13.txt', 'r')

a = file.read()
b = []

b.append(a)

c = ''.join(b)
d = c.replace('\n', '+')

ans = ''.join(list(str(eval(d))))
print(ans[:10])
