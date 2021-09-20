def func(num):
	seq = [num]
	
	while num != 1:
		if num % 2 == 0:
			num = num / 2
			seq.append(int(num))

		else:
			num = 3 * num + 1
			seq.append(int(num))

	return seq

longest_chain = 0
lg_start_num = 0

for n in range(1, 1000001):
	a = func(n)
	b = len(func(n))
	if b > longest_chain:
		longest_chain = b
		lg_start_num = a[0]

print(lg_start_num)