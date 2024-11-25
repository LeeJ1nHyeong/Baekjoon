import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)


def dfs(now, d):
    global turn
    visited[now] = turn
    turn += 1
    depth[now] = d

    for node in tree[now]:
        if depth[node] == -1:
            dfs(node, d + 1)


n, m, r = map(int, input().split())
tree = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)  # 방문 순서
depth = [-1] * (n + 1)  # 깊이

for _ in range(m):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

# 인접 노드 내림차순 정렬
for t in tree:
    t.sort(reverse=True)

turn = 1
dfs(r, 0)

ans = 0
# 방문 순서와 깊이의 곱을 모두 더해서 ans에 저장
for i in range(1, n + 1):
    ans += visited[i] * depth[i]

print(ans)
