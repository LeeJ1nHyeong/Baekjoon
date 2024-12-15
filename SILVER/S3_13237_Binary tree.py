from collections import deque

n = int(input())
tree = [[] for _ in range(n)]
depth = [-1] * n
root = -1

for i in range(n):
    parent = int(input())

    if parent == -1:
        root = i
        continue

    tree[parent - 1].append(i)

queue = deque([root])
depth[root] = 0

while queue:
    now = queue.popleft()

    for node in tree[now]:
        if depth[node] == -1:
            depth[node] = depth[now] + 1
            queue.append(node)

for d in depth:
    print(d)
