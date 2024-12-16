N, D, p = map(int, input().split())
ls = list(map(int,input().split()))

turns = 0
i = 0

while i < N:
    if ls[i] <= 0:
        i += 1
        continue
        
    ls[i] -= D
    turns += 1
    
    if ls[i] < 0 and i + 1 < N:
        overkill_damage = -ls[i]
        next_damage = (overkill_damage * p) // 100  
        ls[i + 1] -= next_damage
    
    if ls[i] <= 0:
        i += 1

print(turns)