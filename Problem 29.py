def func():
	nums = []
	final = []
	for i in range(2, 100+1):
		a = [int(x**i) for x in range(2, 100+1)]
		nums.append(a)
		

	for i in nums:
		for num in i:
			if num not in final:
				final.append(num)
			else:
				pass

	final.sort()

	print(len(final))
func()
