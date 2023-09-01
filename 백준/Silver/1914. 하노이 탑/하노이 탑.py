def hanoi_tower(n, start, end) :
    if n == 1 :
        print(start, end)
        return
       
    hanoi_tower(n-1, start, 6-start-end)
    print(start, end)
    hanoi_tower(n-1, 6-start-end, end)
    
n = int(input())
n1 = n
print(2**n-1)
if 20 >= n:
    hanoi_tower(n, 1, 3)