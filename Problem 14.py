a = []
final = []

def func(n):
    if n == 1:
        a.append(1)

        if len(final) == 0:
            final.append(a)

        else:
            final.append(a)
            

    else:
        if n % 2 == 0:
            a.append(int(n))
            func(n / 2)

        else:
            a.append(int(n))
            func((n * 3) + 1)

func(13)
func(5)
print(final)


# for i in range(2, 11):
#     print(func(i))

# lst2 = sorted(final, key=len)

# print(lst2[-1])