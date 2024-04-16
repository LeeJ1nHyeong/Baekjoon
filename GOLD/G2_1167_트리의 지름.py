def dfs(now, dist):
    global max_end, max_dist
    # 최댓값 여부를 확인하여 그 때의 노드와 거리 최신화
    if dist > max_dist:
        max_end, max_dist = now, dist

    # 현재 노드와 연결되어있는 미방문 노드에 대해 방문 표시 후 dfs 계속 진행
    for node in nodes[now]:
        if not visited[node[0]]:
            visited[node[0]] = 1
            dfs(node[0], dist + node[1])


v = int(input())
nodes = [[] for _ in range(v + 1)]  # 노드 간의 간선을 담을 2차원 리스트

max_end, max_dist = 0, 0  # 1번 노드에서 거리가 가장 먼 노드 번호, 거리

# 노드 간의 간선 정보를 리스트에 저장
for _ in range(v):
    s, *info = map(int, input().split())
    for i in range(0, len(info) - 1, 2):
        e, cost = info[i], info[i + 1]
        nodes[s].append((e, cost))

# 1번 노드에서 가장 멀리 있는 노드와 거리를 찾기 위해 dfs 진행
visited = [0] * (v + 1)
visited[1] = 1
dfs(1, 0)

# 1번 노드에서 가장 멀리 있는 노드를 시작점으로 dfs 추가 진행
visited = [0] * (v + 1)
visited[max_end] = 1
dfs(max_end, 0)

print(max_dist)  # 최댓값 출력
