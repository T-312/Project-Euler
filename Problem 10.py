import math
import random

def random_prime(left, right):
  if min(left, right) <= 0:
    raise RuntimeError('Only natural numbers')
  prime_nums = []
  for i in range(left, right):
    if is_prime(i):
      prime_nums.append(i)
  return prime_nums


def is_prime(num):
  if num <= 2: # 1 and 2 are primes, <= 0 not allowed
    return True
  if not num % 2:
    return False
  for i in range(3, int(math.sqrt(num)) + 1, 2):
    if not num % i  and num != i:
      return False
  return True

nums = random_prime(1, 2000000)
print(sum(nums))