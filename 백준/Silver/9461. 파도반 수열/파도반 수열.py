ls = [1,1,1]
for i in range(101):
    ls.append(ls[i]+ls[i+1])

for _ in range(int(input())):
    print(ls[int(input())-1])