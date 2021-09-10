import sys

sys.setrecursionlimit(10000)

def func(n):
    if n == 1:
        return 1

    if n > 1:
        return n ** n + func(n - 1)

num = str(func(1000))
print(num[-10:])