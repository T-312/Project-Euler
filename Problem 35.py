from itertools import permutations

def is_prime(num):
	a = all(num % i for i in range(2, num))
	return a

def combinations(num):
	a = list(permutations(num))
	b = [int(''.join(map(str, x))) for x in a]
	c = [i for i in b if all(list(map(is_prime, b))) == True]

	return c

def get_length(combinations):
	b = [i for x in combinations for i in x]
	final = []
	for i in b:
		if i not in final:
			final.append(i)

	print(len(final))

def start(nums):
	a = []
	for n in nums:
		if len(combinations(n)) > 0:
			a.append(combinations(n))

	get_length(a)

primes = [str(x) for x in range(2, 1000001) if is_prime(x) == True]
start(primes)