from itertools import permutations
a,b = input().split()
perm = permutations(a,int(b))
perm = sorted(perm)
for i in perm:
    print(''.join(i))
