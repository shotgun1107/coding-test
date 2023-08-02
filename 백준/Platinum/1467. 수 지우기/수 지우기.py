import sys;
from collections import Counter

n = input().strip()
n1 = input().strip()
n2 = Counter(n) - Counter(n1)
answer = ''
idx = 0
while n2:
    for i in range(9,-1,-1):
        i = str(i)
        if n2[i] < 1:
            continue    
        t = n.find(i,idx)

        c = n2 - Counter(n[t:])
        if c:
            continue
        else:
            answer += i
            idx = t + 1
            n2[i] -= 1
            if n2[i] == 0:
                del n2[i]
            break
print(answer)