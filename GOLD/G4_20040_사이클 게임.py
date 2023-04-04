import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

def find(x):
    if x == parent[x]:
        return x
    else:
        return find(parent[x])

def union(x, y):
    p_x = find(x)
    p_y = find(y)
    parent[max(p_x, p_y)] = min(p_x, p_y)
    
N, M = map(int, input().split())
parent = [x for x in range(N)]

turn = 0

for t in range(1, M + 1):
    n1, n2 = map(int, input().split())
    if find(n1) == find(n2):
        turn = t
        break
    union(n1, n2)

print(turn)