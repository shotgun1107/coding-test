import sys

input = sys.stdin.readline

stack1 = []
stack2 = []
anwer = []

c = 0
n = int(input())
for i in range(n):
    stack1.append(int(input()))
i = 0
cc = 0

while True:
    if stack2 and stack1 and stack2[-1] == stack1[0] :
        anwer.append("-")
        stack1.pop(0)
        stack2.pop()
        cc = 0
    elif cc >= n:
        c = 1
        break
    elif stack1:
        anwer.append("+")
        i += 1
        stack2.append(i)
        cc += 1
    else:
        break

if c == 0:
    for i in range(len(anwer)):
        print(anwer[i])
else:
    print("NO")