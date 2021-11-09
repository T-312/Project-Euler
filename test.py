nums = [20, 22, 41, 58, 6, 2, 38, 76]
final = [[a, b, c, d, e] for a in nums for b in nums for c in nums for d in nums for e in nums if int(a-b+c-d+e) == 164 and len(set([a, b, c, d, e])) == 5]
print(final)