from collections import deque

ls = deque(i for i in range(1,int(input())+1))

for i in range(1,5000000):
    if len(ls)  <= 1:
        print(ls[0])
        break
    if not i % 2 == 0:
        ls.popleft()
    else:
        ls.append(ls.popleft())