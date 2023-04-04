import sys
input = sys.stdin.readline

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    p_x, p_y = find(x), find(y)
    parent[max(p_x, p_y)] = min(p_x, p_y)

N = int(input())
M = int(input())
city = [list(map(int, input().split())) for _ in range(N)]
parent = [i for i in range(N + 1)]

for i in range(N):
    for j in range(N):
        if city[i][j]:
            union(i + 1, j + 1)

tour_list = list(map(int, input().split()))

num = parent[tour_list[0]]
ans = 'YES'
for t in tour_list:
    if num != parent[t]:
        ans = 'NO'
        break

print(ans)