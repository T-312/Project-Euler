def d(num):
    divisors = []
    for i in range(1, num):
        if not num % i:
            divisors.append(i)

    return sum(divisors)

def is_amicable(num):
    n1 = d(num)
    n2 = d(n1)
    if n2 == num:
        return sum([n1, n2])

    return 0

already = []
for i in range(10000):
    a = is_amicable(i)
    if a not in already:
        already.append(a)

print(sum(already))
#31626