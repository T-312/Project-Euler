import math

def is_prime(num):
    for n in range(2, int(math.sqrt(num))+1):
        if not num % n:
            return False
    return True

def gen_primes(max_num):
    for i in range(1, max_num, 2):
        if is_prime(i):
            yield i
 
def gen_list(primes, max_val):
    max_length = 0
    max_sum = 0

    for a in range(len(primes)):
        for b in range(a+max_length, max_val):
            current = primes[a:b]
            if sum(current) in primes:
                if len(current) > max_length and sum(current) > max_sum:
                    max_length = len(current)
                    max_sum = sum(current)
                    print(max_sum)
 
    return max_sum
 
num = 100
primes = [i for i in gen_primes(num)]
print(gen_list(primes, num))
