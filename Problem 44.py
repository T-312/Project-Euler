from itertools import permutations

def formula(n):
	return n*(3*n-1)/2

def check_sum(nums):
	return [str(int(a))+str(int(b)) for a in nums for b in nums if a+b in nums]

pent_nums = list(map(formula, range(1, 100)))
print(check_sum(pent_nums))
