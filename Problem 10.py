nums = [x for x in range(0, 1000001) if x != 1 and x % 2 != 0]
final = []
nums.insert(0, 2)

def rem_num(n):
    for i in nums:
        if i > n and i % n == 0:
            nums.remove(i)
rem_num(3)
rem_num(5)
rem_num(7)

for i in nums:
    final.append(str(i))
    final.append('+')

final.pop()
final_sum = eval(''.join(final))
print(final_sum)