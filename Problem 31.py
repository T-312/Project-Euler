# from itertools import permutations
# def func(amount):
#     coins = [1, 2, 5, 10, 20, 50, 100, 200] * amount
#     for i in range(amount+1):
#         for j in list(permutations(coins, i)):
#             if sum(j) == amount:
#                 yield j

# a = [x for x in set(func(5))]
# print(a)
def func(nums, amount):
    a = [1] + [0] * amount
    for 