def is_prime(num):
	if num <= 2:
		return True

	else:
		a = all(num % n for n in range(2, num))
		return a

a = [n for n in range(1, 105000) if is_prime(n)]
print(a[10001])
