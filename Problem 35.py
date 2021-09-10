from itertools import permutations

def is_prime(num):
	a = all(num % i for i in range(2, num))
	return a

def convertTuple(tup):
    str1 = ''
    for item in tup:
        str1 = str1 + item
    return str1

def prime_filter(nums):
	print("Started prime filter")
	final = []
	for n in nums:
		if len(str(n)) == 1:
			final.append(n)
		if len(str(n)) == 2:
			a = list(permutations(str(n)))
			a_list = []
			for i in a:
				a = convertTuple(i)
				a_list.append(a)
			b = all(is_prime(int(i)) for i in a_list)
			if b == True:
				final.append(a)

			else:
				pass

		if len(str(n)) == 3:
			a = list(permutations(str(n)))
			a_list = []
			for i in a:
				a = convertTuple(i)
				a_list.append(a)
			b = all(is_prime(int(i)) for i in a_list)
			if b == True:
				final.append(a)

			else:
				pass

		if len(str(n)) == 4:
			a = list(permutations(str(n)))
			a_list = []
			for i in a:
				a = convertTuple(i)
				a_list.append(a)
			b = all(is_prime(int(i)) for i in a_list)
			if b == True:
				final.append(a)

			else:
				pass

		if len(str(n)) == 5:
			a = list(permutations(str(n)))
			a_list = []
			for i in a:
				a = convertTuple(i)
				a_list.append(a)
			b = all(is_prime(int(i)) for i in a_list)
			if b == True:
				final.append(a)

			else:
				pass

	print(len(final))
	print(final)

primes = []

for i in range(2, 10001):
	a = is_prime(i)
	if a == True:
		primes.append(i)

	else:
		pass

print("Finished generating prime numbers")

prime_filter(primes)