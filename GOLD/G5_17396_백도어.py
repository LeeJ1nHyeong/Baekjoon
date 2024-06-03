import heapq, sys
input = sys.stdin.readline

# 다익스트라
def dijkstra():
    min_cost = [n * 100000] * n  # 각 분기점에 도달하는 최단 시간
    min_cost[0] = 0  # 시작점을 0으로 저장한 상태로 시작

    queue = [(0, 0)]  # 걸린 시간, 분기점 순서로 튜플 형태로 저장

    # 다익스트라 진행
    while queue:
        cost, now = heapq.heappop(queue)

        # 현재 시간이 분기점의 최단시간보다 클 경우 continue
        if cost > min_cost[now]:
            continue

        for next_node, next_cost in nodes[now]:
            # 다음 분기점까지 걸린 시간
            now_cost = cost + next_cost

            # 다음 분기점이 넥서스(마지막 분기점)일 경우 최단 시간 여부 확인
            if next_node == n - 1:
                min_cost[next_node] = min(now_cost, min_cost[next_node])

            # 다음 분기점에 시야가 있을 경우 continue
            if eyesight[next_node]:
                continue

            # now_cost가 다음 분기점의 최단시간일 경우 최단 시간 최신화 후 queue에 추가
            if now_cost < min_cost[next_node]:
                min_cost[next_node] = now_cost
                heapq.heappush(queue, (now_cost, next_node))

    # 넥서스의 최단 시간 값이 변하지 않았을 경우 -1 return
    if min_cost[n - 1] == n * 100000:
        return -1

    return min_cost[n - 1]  # 넥서스까지의 최단 시간 return


n, m = map(int, input().split())
eyesight = list(map(int, input().split()))  # 각 분기점 별 시야 여부
nodes = [[] for _ in range(n)]

# 시작, 끝 분기점의 시간을 양방향으로 저장
for _ in range(m):
    a, b, t = map(int, input().split())
    nodes[a].append((b, t))
    nodes[b].append((a, t))

print(dijkstra())  # 다익스트라 진행
