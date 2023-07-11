sum = 0 
student = []
apple = []
n = int(input())
for _ in range(n):
    x,y = map(int,input().split())
    student.append(x)
    apple.append(y)

for i in range(n):
    if student[i] > apple[i]:
        sum += apple[i]
    else:
        sum += apple[i] % student[i]
print(sum)