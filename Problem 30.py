def func(num):
	num = [int(i)**5 for i in str(num)]
	num = sum(num)
	return int(num)

x = []
for i in range(2, 500000):
	a = func(i)
	if a == i:
		x.append(a)

	else:
		pass

x = sum(x)
print(x)
