from itertools import permutations
ans = list(permutations(list(range(0, 10))))
ans = [str(i) for i in ans[999999]]
ans = ''.join(ans)
print(ans)