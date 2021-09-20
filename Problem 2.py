nums = []
x = 0
y = 1

while x <= 4000000:
    x = x + y
    nums.append(x)
    y = x + y
    nums.append(y)

total = 0

for num in nums:
    if num % 2 == 0 or num % 2 == 0.00:
        total+=num

print(total)