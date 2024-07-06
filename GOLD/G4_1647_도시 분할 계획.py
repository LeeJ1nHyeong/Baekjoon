import sys
input = sys.stdin.readline

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    p_x, p_y = find(x), find(y)
    parent[max(p_x, p_y)] = min(p_x, p_y)

N, M = map(int, input().split())
parent = [i for i in range(N + 1)]
edge = []
min_cost = 0
max_cost = 0

for _ in range(M):
    n1, n2, w = map(int, input().split())
    edge.append([w, n1, n2])

edge.sort()

for i in range(M):
    w, n1, n2 = edge[i]
    if find(n1) != find(n2):
        union(n1, n2)
        min_cost += w
        if w > max_cost:
            max_cost = w

ans = min_cost - max_cost

print(ans)