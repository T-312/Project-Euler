import time
def is_prime(num):
	a = all(num % i for i in range(2, num))
	return a

def gen_primes(num):
	if num <= 1:
		return "Number must be positive"

	nums = list(range(1, num+1, 2))
	primes = [2, 3, 5, 7]

	for n in nums:
		if n % 3 != 0 and n % 5 != 0 and n % 7 != 0:
			primes.append(n)

	primes = sorted(list(set(primes)))
	primes.remove(primes[0])
	return primes

start = time.time()
limit = 100000
length = 0
value = 0
nums = gen_primes(limit)

for a in range(round(len(nums)/3)):
	for b in range(1, len(nums)):
		x = nums[a:b]
		if len(x) > length and sum(x) < limit and is_prime(sum(x)):
			length = len(x)
			value = sum(x)
			print(value)
			for i in range(int(limit/200)):
				nums.pop()

stop = time.time()
print(value)
print("Length:", length)
print("Time:", round(stop-start, 2))