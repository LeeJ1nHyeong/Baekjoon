import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)  # 재귀 제한 설정


def dfs(now):
    global turn
    visited[now] = turn
    turn += 1

    for node in tree[now]:
        if not visited[node]:
            dfs(node)


n, m, r = map(int, input().split())
tree = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

for _ in range(m):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

# 현재 노드의 다음 노드를 내림차순으로 정렬
for t in tree:
    t.sort(reverse=True)

turn = 1
dfs(r)  # 시작 노드부터 dfs 탐색 진행

for i in range(1, n + 1):
    print(visited[i])
