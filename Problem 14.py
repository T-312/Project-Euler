def func(num):
	seq = []
	if num < 2:
		return seq

	else:
		if num % 2 == 0:
			num = num / 2
			seq.append(int(num))

		else:
			num = 3 * num + 1
			seq.append(int(num))
print(func(15))
