def is_prime(num):
	a = all(num % i for i in range(2, num))
	return a

def is_prime_gen(num):
	a = all(num % i for i in range(2, num))
	if a == True:
        return num

    else:
        return None

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

# nums = [int(x) for x in range(8, 750000) if is_prime(x) == True]
# right = [i for i in nums if truncatable_right(i) == True]
# left = [i for i in nums if truncatable_left(i) == True]
# final = [x for x in nums if x in right if x in left]
# print(final)
nums = list(map(is_prime_gen, range(8, 1000)))
print(nums)