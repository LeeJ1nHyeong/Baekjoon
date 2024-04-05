import heapq
import sys
input = sys.stdin.readline


n = int(input())
m = int(input())

nodes = [[] for _ in range(n + 1)]  # 두 간선 간의 가중치를 저장할 2차원 리스트
min_cost = [1000 * 100000 for _ in range(n + 1)]  # 최소 비용을 저장할 리스트

# 두 간선 간 가중치 저장
for _ in range(m):
    s, e, cost = map(int, input().split())
    nodes[s].append((e, cost))

start, end = map(int, input().split())  # 시작점, 도착점

min_cost[start] = 0  # 시작점의 최소비용을 0으로 저장

queue = [(start, 0, [start])]  # 시작점, 최소비용 0, 이동 경로를 튜플 형태로 queue에 저장
min_city = []  # 시작점-도착점 간 최소 비용일 경우의 경로

# 다익스트라
while queue:
    now, cost, city = heapq.heappop(queue)  # 현재 좌표, 비용, 이동 경로
    if min_cost[now] < cost:  # 현재 비용이 좌표의 최소 비용보다 크다면 continue
        continue

    # 다음 경로의 가중치 탐색
    for node in nodes[now]:
        now_cost = min_cost[now] + node[1]
        # 다음 경로 가중치를 더한 값이 더 작다면 최소비용 최신화
        if now_cost < min_cost[node[0]]:
            min_cost[node[0]] = now_cost
            # 이 때 현재 좌표가 도착점이라면 최소 비용 도시 경로 최신화
            if node[0] == end:
                min_city = city + [node[0]]
            heapq.heappush(queue, (node[0], now_cost, city + [node[0]]))

print(min_cost[end])  # 최소 비용 출력
print(len(min_city))  # 최소 비용일 때의 도시 개수 출력
print(*min_city)  # 최소 비용일 때의 경로 출력