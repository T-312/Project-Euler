nums = list(range(1, 401))

for a in nums:
    for b in nums:
        c = (1000 - a) - b
        if a < b < c:
            if a**2 + b**2 == c**2:
                print(a,b,c)
                print(a*b*c)