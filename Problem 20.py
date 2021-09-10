def func(n):
    if n == 1:
        return 1

    if n > 1:
        return n * func(n-1)

nums = [int(i) for i in str(func(100))]
print(sum(nums))