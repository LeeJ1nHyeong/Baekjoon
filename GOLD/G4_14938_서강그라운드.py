import heapq, sys
input = sys.stdin.readline
inf = 1e8

def dijkstra(i):
    queue = []
    distance = [inf] * (N + 1)

    heapq.heappush(queue, [0, i])
    distance[i] = 0

    while queue:
        now_dist, now_place = heapq.heappop(queue)

        for next_dist, next_place in route[now_place]:
            if now_dist + next_dist < distance[next_place]:
                next_dist += now_dist
                distance[next_place] = next_dist
                heapq.heappush(queue, [next_dist, next_place])

    return distance

N, M, R = map(int, input().split())
item = [0] + list(map(int, input().split()))

route = [[] for _ in range(N + 1)]

for _ in range(R):
    s, e, dist = map(int, input().split())
    route[s].append([dist, e])
    route[e].append([dist, s])

max_item = 0

for i in range(1, N + 1):
    item_i = 0
    distance = dijkstra(i)

    for j in range(1, N + 1):
        if distance[j] <= M:
            item_i += item[j]

    max_item = max(max_item, item_i)

print(max_item)