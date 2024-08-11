'''
같은 문양끼리만 이동 가능
탈출이 가능하면 "YES", 불가능하면 "NO" 출력
'''

from collections import deque


def bfs():
    # 원활한 탐색을 위해 반시계방향으로 90도 회전한 형태의 좌표로 변환
    target = prison[w - b][a - 1]  # 시작 위치의 문양

    # bfs 초기 세팅
    visited = [[0] * l for _ in range(w)]
    queue = deque([(w - b, a - 1)])
    visited[w - b][a - 1] = 1

    # bfs 진행
    while queue:
        ci, cj = queue.popleft()

        # 출구에 도착했다면 "YES" return
        if (ci, cj) == (w - d, c - 1):
            return "YES"
        
        # 4방향 탐색
        for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
            ni, nj = ci + di, cj + dj
            
            # 범위를 벗어나면 continue
            if ni < 0 or ni == w or nj < 0 or nj == l:
                continue

            # 다른 문양이라면 continue
            if prison[ni][nj] != target:
                continue

            # 방문 지역이라면 continue
            if visited[ni][nj]:
                continue

            # 방문 표시 후 queue에 추가
            visited[ni][nj] = 1
            queue.append((ni, nj))

    return "NO"  # while문이 종료됐다면 탈출 불가이므로 "NO" return


p = int(input())

for _ in range(p):
    l, w, a, b, c, d = map(int, input().split())
    prison = [list(input()) for _ in range(w)]

    print(bfs())
