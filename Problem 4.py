def is_palindrome(num):
    rev = int(str(num)[::-1])
    return rev == num

nums = list(range(100, 1000))
prods = [a*b for a in nums for b in nums if is_palindrome(a*b)]
print(max(prods))