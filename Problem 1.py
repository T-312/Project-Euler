m3 = [num for num in range(1000) if num % 3 == 0]
m5 = [num for num in range(1000) if num % 5 == 0 and num % 3 != 0]
ans = int(sum(m3) + sum(m5))
print(ans)