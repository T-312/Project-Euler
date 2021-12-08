import math
def is_prime(num):
    if num > 1:
        for n in range(2, int(math.sqrt(num))+1):
            if not num % n:
                return False
        return True
 
def gen_primes(max_num):
    for i in range(1, max_num, 2):
        if i == 3:
            yield 2
        if is_prime(i):
            yield i
 
def gen_list(primes, max_val):
    max_length = 0
    max_sum = 0
 
    for a in range(len(primes)):
        for b in range(a+max_length, max_val):
            current = primes[a:b]
            if len(current) > max_length and sum(current) in primes:
                max_length = len(current)
                max_sum = sum(current)
 
    return max_sum
 
num = 1000000
primes = [i for i in gen_primes(num)]
print(gen_list(primes, num))