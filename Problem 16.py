first_num = 2**1000
first_num = ''.join(str(first_num))
sumlist = []

for i in first_num:
    sumlist.append(i)
    sumlist.append('+')

sumlist.pop()
finalsumlist = ''.join(sumlist)
print(eval(finalsumlist))