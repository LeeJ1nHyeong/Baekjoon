import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    board = [[0 for _ in range(N)] for _ in range(N)]
    si, sj = map(int, input().split())
    ei, ej = map(int, input().split())

    queue = deque()
    queue.append([si, sj])

    while queue:
        i, j = queue.popleft()
        if i == ei and j == ej:
            break
        for di, dj in [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and not board[ni][nj]:
                board[ni][nj] = board[i][j] + 1
                queue.append([ni, nj])
            
    print(board[ei][ej])