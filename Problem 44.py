from itertools import permutations

def formula(n):
	return n*(3*n-1)/2

def check_sum(nums):
	sums = [[a, b, a+b] for a in nums for b in nums if a != b and a+b in nums]
	return sums

def check_dif(nums):
	difs = [[a, b, a - b] for a in nums for b in nums if a != b and a-b in nums]
	return difs

pent_nums = list(map(formula, range(1, 1000)))
difs = [x for x in check_dif(pent_nums)]
sums = [x for x in check_sum(pent_nums)]
final = [x for x in pent_nums if x in difs and x in sums]

print(final)
