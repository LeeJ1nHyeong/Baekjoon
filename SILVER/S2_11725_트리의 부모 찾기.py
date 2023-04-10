import sys
from collections import deque

def bfs(i):
    queue = deque()
    queue.append(i)
    while queue:
        now = queue.popleft()
        for i in tree[now]:
            if parent[i] == 0:
                parent[i] = now
                queue.append(i)

N = int(sys.stdin.readline())
tree = [[] for _ in range(N + 1)]
parent = [0] * (N + 1)

for _ in range(N - 1):
    n1, n2 = map(int, sys.stdin.readline().split())
    tree[n1].append(n2)
    tree[n2].append(n1)

bfs(1)

for i in range(2, N + 1):
    print(parent[i])