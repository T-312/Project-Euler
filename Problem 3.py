def is_prime(num):
    import math
    if num <= 2:
      return True
    if not num % 2:
      return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
      if not num % i  and num != i:
          return False
    return True

def gen_prime_factors(num):
    factors = []
    for i in range(2, num):
        if num % i == 0 and is_prime(i):
            if i not in factors:
                factors.append(i)

    return factors

print(max(gen_prime_factors(600851475143)))