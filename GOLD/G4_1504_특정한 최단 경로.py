import heapq, sys
input = sys.stdin.readline

# 다익스트라
def dijkstra(start, end):
    min_dist = [200000 * 1000] * (n + 1)  # 구간 별 최단 경로를 저장할 리스트
    min_dist[start] = 0  # 시작 지점의 최단 경로값을 0으로 변경
    queue = []  # 우선순위 큐
    heapq.heappush(queue, (0, start))  # (이동거리, 현재 정점 번호)를 튜플 형태로 queue에 저장

    # 다익스트라 진행
    while queue:
        dist, now = heapq.heappop(queue)

        # 현재 경로값이 정점의 최단경로보다 높다면 continue
        if dist > min_dist[now]:
            continue

        # 현재 정점의 다음 이동 경로의 경로값과 비교하여 최소 경로 여부 확인 후 queue에 저장
        for node in nodes[now]:
            now_dist = dist + node[1]
            if now_dist < min_dist[node[0]]:
                min_dist[node[0]] = now_dist
                heapq.heappush(queue, (now_dist, node[0]))

    return min_dist[end]  # 도착점까지의 최단 경로 return


n, e = map(int, input().split())
nodes = [[] for _ in range(n + 1)]  # 노드 간의 간선을 저장할 2차원 리스트

# 노드 간의 간선 정보를 양방향으로 저장
for _ in range(e):
    s, e, d = map(int, input().split())
    nodes[s].append((e, d))
    nodes[e].append((s, d))

v1, v2 = map(int, input().split())  # 반드시 지나가야 할 두 정점

# 시작점 -> v1 -> v2 -> 도착점 순서로 다익스트라 진행
v1v2 = 0
v1v2 += dijkstra(1, v1)
v1v2 += dijkstra(v1, v2)
v1v2 += dijkstra(v2, n)

# 시작점 -> v2 -> v1 -> 도착점 순서로 다익스트라 진행
v2v1 = 0
v2v1 += dijkstra(1, v2)
v2v1 += dijkstra(v2, v1)
v2v1 += dijkstra(v1, n)

# 두 값의 최솟값이 200000 * 1000을 넘기면 -1 출력, 아니면 최솟값 출력
print(min(v1v2, v2v1) if min(v1v2, v2v1) < 200000 * 1000 else -1)
