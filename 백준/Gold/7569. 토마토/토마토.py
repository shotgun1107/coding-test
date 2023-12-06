# from collections import deque
# import sys
# input = sys.stdin.readline

# M,N = map(int,input().split())
# ls = []
# check = []
# bfs = deque()

# for i in range(N):
#     ls.append(s := list(map(int,input().split())))
#     check.extend(s)
#     idx = [index for index, value in enumerate(s) if value == 1]
#     for j in idx:
#         bfs.append((i,j))


# nx_ls = [-1,1,0,0]
# ny_ls = [0,0,-1,1]

# c = 0
# m = 1

# while bfs:
#     x,y = bfs.popleft()
#     for i in range(4):
#         nx = x + nx_ls[i]
#         ny = y + ny_ls[i]
#         if nx < 0 or nx >= N or ny < 0 or ny >= M:
#             continue
#         if ls[nx][ny] == 0:
#             bfs.append((nx,ny))
#             ls[nx][ny] = ls[x][y] + 1
#             m = max(m,ls[x][y] + 1)
#             check[nx*M+ny] = 1
# print(m-1 if check.count(0) == 0 else -1)

from collections import deque
import sys
input = sys.stdin.readline

M, N, H = map(int, input().split())
ls = []
check = []
bfs = deque()

for i in range(H):
    ls.append([])
    for j in range(N):
        ls[i].append(s := list(map(int, input().split())))
        check.extend(s)
        idx = [index for index, value in enumerate(s) if value == 1]
        for k in idx:
            bfs.append((i, j, k))

nx_ls = [-1, 1, 0, 0, 0, 0]
ny_ls = [0, 0, -1, 1, 0, 0]
nz_ls = [0, 0, 0, 0, -1, 1]

c = 0
m = 1

while bfs:
    x, y, z = bfs.popleft()
    for i in range(6):
        nx = x + nx_ls[i]
        ny = y + ny_ls[i]
        nz = z + nz_ls[i]
        if nx < 0 or nx >= H or ny < 0 or ny >= N or nz < 0 or nz >= M:
            continue
        if ls[nx][ny][nz] == 0:
            bfs.append((nx, ny, nz))
            ls[nx][ny][nz] = ls[x][y][z] + 1
            m = max(m, ls[x][y][z] + 1)
            check[nx * N * M + ny * M + nz] = 1

print(m - 1 if check.count(0) == 0 else -1)
