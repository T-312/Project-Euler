def multiplication(nums):
    ways = 0
    for i in range(1, max(nums)+1):
        for n in nums:
            if i * n == 200:
                ways+=1

    return ways

def add(nums):
    


coins = [1, 2, 5, 10, 20, 50, 100, 200]