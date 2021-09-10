nums = list(range(100, 1000))
final = []

for a in nums:
    for b in nums:
        for c in nums:
            d = a * b * c
            if str(d) == str(d)[::-1]:
                final.append(d)

final.sort()
print(final[-1])