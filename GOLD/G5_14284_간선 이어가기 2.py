import heapq, sys
input = sys.stdin.readline


n, m = map(int, input().split())
nodes = [[] for _ in range(n + 1)]  # 노드 간의 간선 가중치를 저장할 2차원 리스트

# 노드 간의 간선 가중치를 양방향으로 저장
for _ in range(m):
    a, b, c = map(int, input().split())
    nodes[a].append((b, c))
    nodes[b].append((a, c))

s, t = map(int, input().split())  # 시작점, 도착점

min_cost = [5000 * 100] * (n + 1)  # 최소 비용을 저장할 리스트
# 시작점의 최소 비용을 0으로 저장 후 queue에 (비용, 정점)의 튜플 형태로 queue에 저장
min_cost[s] = 0
queue = [(0, s)]

# 다익스트라 진행
while queue:
    cost, now = heapq.heappop(queue)

    if cost > min_cost[now]:
        continue

    for node in nodes[now]:
        now_cost = cost + node[1]
        if now_cost < min_cost[node[0]]:
            min_cost[node[0]] = now_cost
            heapq.heappush(queue, (now_cost, node[0]))

print(min_cost[t])  # 도착점에서의 최소 비용 출력
