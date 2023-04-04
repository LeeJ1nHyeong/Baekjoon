import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    p_x, p_y = find(x), find(y)
    parent[max(p_x, p_y)] = min(p_x, p_y)

N, M = map(int, input().split())
parent = [i for i in range(N + 1)]

for _ in range(M):
    check, a, b = map(int, input().split())
    if check == 0:
        union(a, b)
    elif check == 1:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')