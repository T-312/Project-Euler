nums = list(range(3, 105000))

def prime(num):
    a = []
    if num > 1:
        for i in range(2, num):
            if num > 3:
                if num % 3 == 0:
                    a.append('no')
            if num > 5:
                if num % 5 == 0:
                    a.append('no')
            
            if num > 7:
                if num % 7 == 0:
                    a.append('no')

            if num % i == 0:
                a.append('no')

            else:
                a.append(str(num))

    else:
        a.append('no')

    return a[0]
    a.clear()

print("Making list...")
main = list(map(prime, nums))
main.insert(0, '2')
print("Removing the 'no' from the list...")
while 'no' in main:
    main.remove('no')

print(main[10000])

#104743