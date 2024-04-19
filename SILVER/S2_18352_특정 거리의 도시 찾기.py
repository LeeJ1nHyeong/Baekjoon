import heapq, sys
input = sys.stdin.readline


n, m, k, x = map(int, input().split())
nodes = [[] for _ in range(n + 1)]  # 노드 간선 정보를 담을 2차원 리스트

# 노드 간선 정보 저장
for _ in range(m):
    s, e = map(int, input().split())
    nodes[s].append(e)

# 최단 거리 정보를 저장할 리스트, 최댓값이 300000이므로 300001로 리스트 생성
min_dist = [300001] * (n + 1)

# 시작점 번호의 최단거리를 0으로 설정 후 queue에 (거리, 노드 번호) 튜플 형태로 추가
min_dist[x] = 0
queue = [(0, x)]

ans = []  # x번에서 출발하여 최단 거리가 k인 번호를 담을 리스트

# 다익스트라 진행
while queue:
    dist, now = heapq.heappop(queue)
    if dist > min_dist[now]:
        continue

    for node in nodes[now]:
        now_dist = dist + 1
        if now_dist < min_dist[node]:
            min_dist[node] = now_dist
            # 다음 번호까지의 최단 거리가 k라면 ans에 저장
            if now_dist == k:
                ans.append(node)
            # k가 아닐 경우 queue에 heappush 진행
            else:
                heapq.heappush(queue, (now_dist, node))

# 최단거리가 k인 번호가 없을 경우 -1 출력
if not ans:
    print(-1)
else:  # 최단거리가 k인 번호가 있을 경우, 오름차순 정렬 후 순서대로 출력
    ans.sort()
    for a in ans:
        print(a)
