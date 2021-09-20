def gen_multiples(num):
	multiples = []
	for i in range(1, num):
		if num % i == 0:
			multiples.append(i)

	return multiples

def check_nums(multiples):
	nums = list(range(1, 20+1))
	num_range = []
	for i in nums:
		if i in multiples:
			num_range.append(int(i))

	return num_range == nums

nums = [x for x in range(1, 10000) if check_nums(gen_multiples(x))]
print(nums)
