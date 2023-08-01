import heapq
N = int(input())
ls = []
sum = 0 
for _ in range(N): 
    heapq.heappush(ls, int(input()))
while len(ls) > 1:
    min1 = heapq.heappop(ls)
    min2 = heapq.heappop(ls)
    M = min1 + min2
    heapq.heappush(ls, M)
    sum += M
print(sum)