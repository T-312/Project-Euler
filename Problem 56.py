def gen_nums():
    max_sum = 0
    for a in range(100):
        for b in range(100):
            num = [int(x) for x in f'{a**b}']
            if sum(num) > max_sum:
                max_sum = sum(num)

    return max_sum

print(gen_nums())