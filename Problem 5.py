num = 1
divisors = []
non_divisors = []
while len(non_divisors) != 0:
    for i in range(1, 10):
        if num % i == 0:
            divisors.append(i)

        else:
            non_divisors.append(i)
            num+=1

    if len(non_divisors) == 0:
        print(divisors)
    
    else:
        divisors.clear()
        non_divisors.clear()