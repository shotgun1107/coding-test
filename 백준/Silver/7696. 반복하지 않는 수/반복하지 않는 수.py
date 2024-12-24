from itertools import permutations, chain, islice
import math, sys

while True:
    if (c:=int(sys.stdin.readline()))==0: break
    result = next(islice(chain(*map(lambda l: islice(permutations(range(10),l), math.perm(9,l-1), None), range(1,11))), c-1, None))
    print(''.join(map(str,result)))