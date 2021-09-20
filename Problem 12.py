def gen_tri_nums(num):
	if num > 1:
		nums = [n for n in range(1, num)]
		return sum(nums)

	else:
		pass

def gen_divisors(num):
	divs = [n for n in range(1, num+1) if num % n == 0]
	return divs

#tri_nums = list(map(gen_tri_nums, range(1, 1000000)))
tri_nums = [gen_tri_nums(x) for x in range(1, 8000000)]
for i in tri_nums:
	if len(gen_divisors(i)) >= 500:
		print(i)
		exit()
