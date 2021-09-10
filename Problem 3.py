# num = 600851475143
# factors = [x for x in range(2, num) if num % x == 0]
# def exclude(x):
#     for num in factors:
#         if num > x and num % x == 0:
#             factors.remove(num)

# def loop():
#     exclude(2)
#     exclude(3)
#     exclude(5)
#     exclude(7)
#     exclude(11)
#     exclude(13)

# loop()
# loop()

# print(factors[-1])

def primes(num):
    a = [i for i in range(1, num) if num % i == 0]
    for i in a:
        for n in range(i+1, num):
            if i % n in a:
                a.remove(n)

    print(a)

primes(13195)