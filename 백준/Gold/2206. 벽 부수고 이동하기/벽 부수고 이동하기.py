from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[[0,0] for _ in range(m)] for _ in range(n)]

queue = deque([(0, 0, 0)])
visited[0][0][0] = 1

while queue:
    x, y, z = queue.popleft()
    if x == n - 1 and y == m - 1:
        print(visited[x][y][z])
        break

    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 1 and z == 0:
                visited[nx][ny][1] = visited[x][y][0] + 1
                queue.append((nx, ny, 1))
            elif graph[nx][ny] == 0 and visited[nx][ny][z] == 0:
                visited[nx][ny][z] = visited[x][y][z] + 1
                queue.append((nx, ny, z))
else:
    print(-1)