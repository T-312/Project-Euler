def formula(n):
	return n*(3*n-1)/2

a = list(range(1, 11))
pentagonal_nums = list(map(formula, a))

print(pentagonal_nums)
