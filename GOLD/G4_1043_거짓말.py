import sys

def dfs(now):
    visited[now] = True
    for i in party[now]:
        for j in party_member[i]:
            if not visited[j]:
                dfs(j)

N, M = map(int, sys.stdin.readline().split())
T_cnt, *T = map(int, sys.stdin.readline().split())
visited = [False] * (M + 1)

party_cnt = M
party = [[]]
party_member = [[] for _ in range(N + 1)]

for i in range(1, M + 1):
    P_cnt, *P = map(int, sys.stdin.readline().split())
    party.append(P)
    for p in P:
        party_member[p].append(i)

if not T:
    print(M)

else:
    for t in T:
        for pm in party_member[t]:
            if not visited[pm]:
                dfs(pm)

    print(visited.count(False) - 1)