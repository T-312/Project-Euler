def is_prime(num):
        a = all(num % i for i in range(2, num))
        return a

def primes(n): #This function was borrowed - more optimised version of prime number generator
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

def truncatable_left(num):
    num = [i for i in str(num)]
    nums = []
    x = -1
    for i in num:
        a = int(''.join(num[x:]))
        x-=1
        nums.append(a)
        
        if len(nums) == len(num):
            if 1 in nums:
                return False

            else:
                final = all([is_prime(num) for num in nums])
                return final

def truncatable_right(num):
    num = [i for i in str(num)]
    nums = []
    x = 1
    for i in num:
        a = int(''.join(num[:x]))
        x+=1
        nums.append(a)

        if len(nums) == len(num):
            if 1 in nums:
                return False

            else:
                final = all([is_prime(num) for num in nums])
                return final

nums = primes(750000)
right = [i for i in nums if truncatable_right(i) == True]
left = [i for i in nums if truncatable_left(i) == True]
banned = [2, 3, 5, 7]
final = [x for x in nums if x in right if x in left if x not in banned]
print(sum(final))
