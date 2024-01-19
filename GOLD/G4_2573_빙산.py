'''
1. 빙산을 탐색하여 주변 4방향 중 바다인 칸의 개수를 구하고 현재 빙산 값에 그 값을 빼서 저장 (melt 함수 실행)
2. 녹은 빙산을 탐색하여 빙산이 분리됐는지 확인 (check 함수 실행)
    2-1. check()의 return 값이 1이면 year 1 추가 후 위 과정 반복
    2-2. check()의 return 값이 2 이상이면 종료
    2-3. check()의 return 값이 0이면 year을 0으로 바꾸고 종료
'''

from collections import deque

def melt():  # 빙산 녹이기
    next_iceberg = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if iceberg[i][j]:
                # 주변 바다 개수 만큼 빙산 녹이기
                next_iceberg[i][j] = iceberg[i][j] - search_sea(i, j)
                # 녹은 빙산 값이 음수라면 0으로 저장
                if next_iceberg[i][j] < 0:
                    next_iceberg[i][j] = 0

    return next_iceberg  # 탐색 완료 후 녹은 빙산 return

def search_sea(i, j):  # 4방향 중 바다가 몇 군데인지 탐색
    sea = 0  # 바다 개수
    for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
        ni, nj = i + di, j + dj
        if iceberg[ni][nj] == 0:
            sea += 1

    return sea

def check():  # 녹은 빙산 탐색
    cnt = 0  # 빙산 덩어리 개수
    visited = [[0] * m for _ in range(n)]  # 방문 여부 체크

    for i in range(n):
        for j in range(m):
            # 해당 위치가 빙산이고 미방문 지역이라면 bfs 진행
            if iceberg[i][j] and not visited[i][j]:
                queue = deque([(i, j)])
                visited[i][j] = 1

                while queue:
                    now_i, now_j = queue.popleft()
                    for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
                        ni, nj = now_i + di, now_j + dj
                        if iceberg[ni][nj] and not visited[ni][nj]:
                            visited[ni][nj] = 1
                            queue.append((ni, nj))

                cnt += 1  # bfs 종료 후 빙산 덩어리 1 추가

    return cnt

n, m = map(int, input().split())
iceberg = [list(map(int, input().split())) for _ in range(n)]

year = 1  # 빙산이 분리되는데 걸리는 시간
while True:
    iceberg = melt()  # 녹은 빙산을 iceberg에 새로 저장

    cnt = check()  # 빙산 덩어리 개수 저장

    if cnt == 0:  # 빙산 덩어리가 없다면 year를 0으로 저장하고 while문 종료
        year = 0
        break
    elif cnt >= 2:  # 빙산 덩어리가 2개 이상이면 while문 바로 종료
        break

    year += 1  # 빙산 덩어리가 1개면 year 1 추가

print(year)