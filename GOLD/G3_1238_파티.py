import heapq
import sys
input = sys.stdin.readline


n, m, x = map(int, input().split())
nodes = [[] for _ in range(n + 1)]  # 노드간의 간선 가중치를 저장할 2차원 리스트

# 단방향이므로 시작점에 (도착점, 이동 시간)을 튜플 형태로 저장
for _ in range(m):
    s, e, cost = map(int, input().split())
    nodes[s].append((e, cost))

# x번에서 다른 지점까지 걸리는 최소 시간
queue = [(0, x)]
from_x = [10000 * 100] * (n + 1)
from_x[x] = 0

# 다익스트라 진행
while queue:
    cost, now = heapq.heappop(queue)
    if from_x[now] < cost:
        continue

    for node in nodes[now]:
        now_cost = cost + node[1]
        if now_cost < from_x[node[0]]:
            from_x[node[0]] = now_cost
            heapq.heappush(queue, (now_cost, node[0]))

# 각 학생들이 x번으로 가는 데에 걸리는 최소 시간
to_x = [10000 * 100] * (n + 1)
to_x[x] = 0

# x번을 제외한 모든 지점을 시작점으로하는 다익스트라 진행
for i in range(1, n + 1):
    if i != x:
        temp = [10000 * 100] * (n + 1)
        temp[i] = 0
        queue2 = [(0, i)]
        while queue2:
            cost, now = heapq.heappop(queue2)
            if temp[now] < cost:
                continue

            for node in nodes[now]:
                now_cost = cost + node[1]
                if node[0] == x:
                    temp[x] = min(temp[x], now_cost)
                else:
                    if now_cost < temp[node[0]]:
                        temp[node[0]] = now_cost
                        heapq.heappush(queue2, (now_cost, node[0]))

        to_x[i] = temp[x]

# 두 시간의 합 중 최댓값을 출력
ans = 0
for i in range(1, n + 1):
    ans = max(ans, from_x[i] + to_x[i])

print(ans)