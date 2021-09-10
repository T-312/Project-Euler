def square(num):
    return num ** 2

nums = list(range(0, 101))
squared_nums = list(map(square, nums))

a = []

for num in squared_nums:
    a.append(str(num))
    a.append('+')

a.pop()
b = ''.join(a)

squared_nums_final = eval(b)

nums = list(range(0, 101))

a = []

for num in nums:
    a.append(str(num))
    a.append('+')

a.pop()
c = ''.join(a)

non_squared_nums = int(eval(c))
non_sq_final = non_squared_nums ** 2

print(non_sq_final - squared_nums_final)