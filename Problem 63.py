def gen_nums():
    for y in range(1, 100):
        for x in range(1, 100):
            yield (f'{x ** y}', y)

nums = gen_nums()
a = 0
for i in nums:
    if len(i[0]) == i[1]:
        a+=1

print(a)