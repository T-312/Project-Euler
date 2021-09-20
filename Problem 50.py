def gen_primes(num):
	if num <= 1:
		return "Number must be positive"

	nums = list(range(1, num+1, 2))
	primes = [2, 3, 5, 7]

	for n in nums:
		if n % 3 != 0 and n % 5 != 0 and n % 7 != 0:
			primes.append(n)

	primes = sorted(list(set(primes)))
	primes.pop(0)
	return primes

largest_sum = 0
limit = 1000
nums = gen_primes(limit)
sums = []
final = []

for n in nums:
	sums.append(n)
	if sum(sums) in nums:
		final.append(sum(sums))
print(final)
