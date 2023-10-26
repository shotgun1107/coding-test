input()
print('Happy' if sum([-1 if i % 2 else 1 for i in list(map(int,input().split()))]) > 0 else 'Sad')