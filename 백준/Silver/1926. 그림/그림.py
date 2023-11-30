from collections import deque

ls = []
a,b = map(int,input().split())

for _ in range(a):
    ls.append(list(map(lambda x: [int(x), 0], input().split())))

answer_count = 0
max_num = 0

for i in range(a):
    check = deque()
    for j in range(b):
        if ls[i][j][0] == 1 and ls[i][j][1] == 0:
            check.append((i,j))
            m = 0
            answer_count += 1
            while check:
                # print(check)
                x, y = check.popleft()
                ls[x][y][1] = 1
                m += ls[x][y][0]
                top = (x-1,y) if x-1 >= 0 and ls[x-1][y][1] != 1 else -1
                bottom = (x+1,y) if x+1 <= a - 1 and ls[x+1][y][1] != 1  else -1
                left = (x,y-1) if y-1 >= 0 and ls[x][y-1][1] != 1 else -1
                right = (x,y+1) if y+1 <= b-1 and ls[x][y+1][1] != 1 else -1
                for k in [top,bottom,left,right]:
                    if not k == -1:
                        nx , ny = k
                        ls[nx][ny][1] = 1
                        if ls[nx][ny][0] == 1:
                            check.append(k)
            # print('------------')
            max_num = max(max_num,m)
print(answer_count,max_num)

