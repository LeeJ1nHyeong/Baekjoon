import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)  # 재귀 제한 설정


def dfs(now, d):
    # 탐색 노드의 깊이 저장
    depth[now] = d

    # 미방문 노드를 탐색하여 dfs 진행
    for node in tree[now]:
        if depth[node] == -1:
            dfs(node, d + 1)


n, m, r = map(int, input().split())
tree = [[] for _ in range(n + 1)]
depth = [-1] * (n + 1)

for _ in range(m):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

# 인접 노드 오름차순 정렬
for t in tree:
    t.sort()

dfs(r, 0)  # 루트 노드부터 dfs 탐색 진행

for i in range(1, n + 1):
    print(depth[i])
