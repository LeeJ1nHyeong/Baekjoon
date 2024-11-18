from collections import deque
import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
tree = [[] for _ in range(n + 1)]
depth = [-1] * (n + 1)  # 트리 내 루트 노드로부터의 깊이

for _ in range(m):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

queue = deque()
queue.append((r, 0))
depth[r] = 0

while queue:
    now, d = queue.popleft()

    for node in tree[now]:
        if depth[node] != -1:
            continue

        depth[node] = d + 1
        queue.append((node, d + 1))

for i in range(1, n + 1):
    print(depth[i])
