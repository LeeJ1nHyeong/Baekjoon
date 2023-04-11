from collections import deque

M, N = map(int, input().split())
C = int(input())

block = [[''] * (M + 1) for _ in range(N + 1)]

for i in range(M + 1):
    block[0][i] = block[N][i] = 0

for i in range(N + 1):
    block[i][0] = block[i][M] = 0

for i in range(1, C + 1):
    d, a = map(int, input().split())
    if d == 1:
        block[0][a] = i
    elif d == 2:
        block[N][a] = i
    elif d == 3:
        block[a][0] = i
    elif d == 4:
        block[a][M] = i

guard_d, g = map(int, input().split())

if guard_d == 1:
    guard = [0, g]
elif guard_d == 2:
    guard = [N, g]
elif guard_d == 3:
    guard = [g, 0]
elif guard_d == 4:
    guard = [g, M]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

sum_short = 0

for a in range(1, C + 1):
    visited = [[False] * (M + 1) for _ in range(N + 1)]
    queue = deque()
    queue.append(guard + [0])
    while queue:
        i, j, cnt = queue.popleft()
        visited[i][j] = True
        if block[i][j] == a:
            sum_short += cnt
            break
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < N + 1 and 0 <= nj < M + 1 and block[ni][nj] != '' and not visited[ni][nj]:
                queue.append([ni, nj, cnt + 1])

print(sum_short)