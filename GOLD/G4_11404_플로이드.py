import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
min_cost = [[1e9 for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        if i == j:
            min_cost[i][j] = 0

for _ in range(M):
    i, j, cost = map(int, input().split())
    min_cost[i - 1][j - 1] = min(min_cost[i - 1][j - 1], cost)

for k in range(N):
    for i in range(N):
        for j in range(N):
            min_cost[i][j] = min(min_cost[i][j], min_cost[i][k] + min_cost[k][j])

for i in range(N):
    for j in range(N):
        if min_cost[i][j] == 1e9:
            print(0, end=" ")
        else:
            print(min_cost[i][j], end=" ")
    print()