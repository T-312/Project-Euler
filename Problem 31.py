def multiplication(nums):
    ways = 0
    for i in range(1, max(nums)+1):
        for n in nums:
            if i * n == 200:
                ways+=1

    return ways

def add(nums):
	ways = 0
	for a in nums:
		for b in range(max(nums)):
			if a * b == 200:
				ways+=1

	return ways


coins = [1, 2, 5, 10, 20, 50, 100, 200]
print(multiplication(coins) + add(coins))
