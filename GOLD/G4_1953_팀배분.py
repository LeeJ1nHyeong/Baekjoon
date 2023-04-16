import sys

def dfs(now):
    visited[now] = True
    for i in hate[now]:
        if not visited[i]:
            if now in team_blue:
                team_white.append(i)
            else:
                team_blue.append(i)
            dfs(i)

N = int(sys.stdin.readline())
hate = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
team_blue = []
team_white = []

for i in range(1, N + 1):
    H_cnt, *H = map(int, sys.stdin.readline().split())
    for h in H:
        hate[h].append(i)

for i in range(1, N + 1):
    if not visited[i]:
        team_blue.append(i)
        dfs(i)

team_blue.sort()
team_white.sort()
print(len(team_blue))
for tb in team_blue:
    print(tb, end=' ')
print()
print(len(team_white))
for tw in team_white:
    print(tw, end=' ')