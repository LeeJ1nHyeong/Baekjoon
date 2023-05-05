import sys
from collections import deque
input = sys.stdin.readline


def dfs(V):
    visited_dfs[V] = True
    print(V, end=' ')
    for i in range(1, N + 1):
        if node[V][i] == 1 and visited_dfs[i] == 0:
            dfs(i)

def bfs(V):
    queue = deque()
    queue.append(V)
    visited_bfs[V] = 1
    while queue:
        now = queue.popleft()
        print(now, end = ' ')
        for i in range(1, N + 1):
            if not visited_bfs[i] and node[now][i] == 1:
                queue.append(i)
                visited_bfs[i] = True


N, M, V = map(int, input().split())

node = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    node[a][b] = node[b][a] = 1

visited_dfs = [False] * (N + 1)
visited_bfs = [False] * (N + 1)

dfs(V)
print()
bfs(V)