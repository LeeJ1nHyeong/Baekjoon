import heapq


def dijkstra():
    min_cost = [[10 * n * n] * n for _ in range(n)]  # 각 위치까지의 최소 비용을 저장할 2차원 리스트
    # 시작 위치의 최소 비용 값을 cave의 처음 위치로 저장
    min_cost[0][0] = cave[0][0]
    queue = [(cave[0][0], 0, 0)]

    # 다익스트라 진행
    while queue:
        cost, i, j = heapq.heappop(queue)
        if min_cost[i][j] < cost:
            continue

        # 현재 위치를 기준으로 4방향 델타탐색 진행
        for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
            ni, nj = i + di, j + dj
            # 다음 위치가 도착점이라면 현재 비용과 도착점의 비용을 더한 값을 return
            if ni == n - 1 and nj == n - 1:
                return cost + cave[ni][nj]
            
            # 다음 위치의 비용을 더한 값이 최소 비용이라면 해당 값을 리스트에 새로 저장 후, 좌표와 함께 queue에 heappush 진행
            if 0 <= ni < n and 0 <= nj < n:
                now_cost = cost + cave[ni][nj]
                if min_cost[ni][nj] > now_cost:
                    min_cost[ni][nj] = now_cost
                    heapq.heappush(queue, (now_cost, ni, nj))


num = 1  # 문제 번호
while True:
    n = int(input())
    if n == 0:  # n이 0일 경우 종료
        break

    cave = [list(map(int, input().split())) for _ in range(n)]
    print(f"Problem {num}: {dijkstra()}")  # 문제 형식에 맞게 출력

    num += 1  # 문제 번호 1 증가
