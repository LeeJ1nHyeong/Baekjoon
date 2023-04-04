import sys
input = sys.stdin.readline

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    p_x, p_y = find(x), find(y)
    parent[max(p_x, p_y)] = min(p_x, p_y)

V, E = map(int, input().split())
parent = [i for i in range(V + 1)]

edge = []
min_cost = 0

for _ in range(E):
    a, b, c = map(int, input().split())
    edge.append((c, a, b))

edge.sort()

for i in range(E):
    cost, n1, n2 = edge[i]
    if find(n1) != find(n2):
        union(n1, n2)
        min_cost += cost

print(min_cost)