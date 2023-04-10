import sys
from collections import deque
input = sys.stdin.readline

def dfs(i, j, trace):
    global cnt
    queue = deque()
    queue.append([i, j])

    while True:
        si, sj = queue.popleft()
        if visited[si][sj]:
            if visited[si][sj] == trace:
                cnt += 1
            return

        visited[si][sj] = trace

        if move[si][sj] == 'L':
            queue.append([si, sj - 1])
        elif move[si][sj] == 'R':
            queue.append([si, sj + 1])
        elif move[si][sj] == 'U':
            queue.append([si - 1, sj])
        elif move[si][sj] == 'D':
            queue.append([si + 1, sj])

N, M = map(int, input().split())
move = [list(str(input())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]

cnt = 0
trace = 1

for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            dfs(i, j, trace)
            trace += 1

print(cnt)