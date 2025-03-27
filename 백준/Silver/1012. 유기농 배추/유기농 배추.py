import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(int(input())):
    M, N, K = map(int, input().split())
    grid = [[0] * M for _ in range(N)]
    
    for _ in range(K):
        x, y = map(int, input().split())
        grid[y][x] = 1

    count = 0
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 1:
                count += 1
                queue = deque([(i, j)])
                grid[i][j] = 0
                while queue:
                    x, y = queue.popleft()
                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]
                        if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] == 1:
                            grid[nx][ny] = 0
                            queue.append((nx, ny))
    print(count)
