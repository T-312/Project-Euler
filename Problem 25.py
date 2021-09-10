nums = ['1']
x = 0
y = 1

while len(nums[-1]) != 1000:
    x = int(x) + int(y)
    nums.append(str(x))
    y = int(x) + int(y)
    nums.append(str(y))

    if len(nums[-1]) == 1000:
        final = [num for num in nums if len(num) == 1000]
        print(nums.index(final[-1]))
        exit()

