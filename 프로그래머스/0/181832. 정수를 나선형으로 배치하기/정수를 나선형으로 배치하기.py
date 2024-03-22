def solution(n):
    matrix = [[0] * n for _ in range(n)]
    count = 1
    direction = 0
    row, col = 0, 0

    while count <= n * n:
        matrix[row][col] = count
        count += 1
        if direction == 0:
            if col + 1 < n and matrix[row][col + 1] == 0:
                col += 1
            else:
                direction = 1
                row += 1
        elif direction == 1:
            if row + 1 < n and matrix[row + 1][col] == 0:
                row += 1
            else:
                direction = 2
                col -= 1
        elif direction == 2:
            if col - 1 >= 0 and matrix[row][col - 1] == 0:
                col -= 1
            else:
                direction = 3
                row -= 1
        else:
            if row - 1 >= 0 and matrix[row - 1][col] == 0:
                row -= 1
            else:
                direction = 0
                col += 1

    return matrix
