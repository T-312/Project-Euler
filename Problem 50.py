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
limit = 400
nums = gen_primes(limit)

for i in range(limit):
	a = sum(nums[:i])
	if a > largest_sum and a in nums:
		largest_sum = sum(nums[:i])
		print(nums[:i])

print(largest_sum)
