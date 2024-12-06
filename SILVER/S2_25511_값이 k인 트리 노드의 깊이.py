from collections import deque


def bfs():
    queue = deque([0])

    while queue:
        now = queue.popleft()

        if num[now] == k:
            return depth[now]

        for node in tree[now]:
            depth[node] = depth[now] + 1
            queue.append(node)


n, k = map(int, input().split())
tree = [[] for _ in range(n)]
depth = [0] * n

for _ in range(n - 1):
    p, c = map(int, input().split())
    tree[p].append(c)

num = list(map(int, input().split()))

print(bfs())
