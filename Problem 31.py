from itertools import permutations
def func(amount):
    for i in range(amount+1):
        coins = [1, 2, 5, 10, 20, 50, 100, 200] * int(i)
        for j in list(permutations(coins, i)):
            if sum(j) == amount:
                yield j

a = [x for x in set(func(5))]
print(a)