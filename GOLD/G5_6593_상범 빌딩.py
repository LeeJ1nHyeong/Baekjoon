from collections import deque


def bfs():
    visited = [[[0 for _ in range(c)] for _ in range(r)] for _ in range(l)]  # 방문 여부 체크용 3차원 리스트
    queue = deque()

    # 시작 지점을 찾아 좌표를 queue에 저장
    for i in range(l):
        for j in range(r):
            for k in range(c):
                if building[i][j][k] == "S":
                    queue.append((i, j, k, 0))
                    visited[i][j][k] = 1
                    break
    
    # bfs 진행
    while queue:
        i, j, k, move = queue.popleft()

        for di, dj, dk in (1, 0, 0), (-1, 0, 0), (0, 0, 1), (0, 1, 0), (0, 0, -1), (0, -1, 0):
            ni, nj, nk = i + di, j + dj, k + dk
            if 0 <= ni < l and 0 <= nj < r and 0 <= nk < c:
                # 다음 좌표가 도착지점이라면 문제 조건에 맞게 return
                if building[ni][nj][nk] == "E":
                    return f"Escaped in {move + 1} minute(s)."
                # 이동 가능한 미방문 지역일 경우 방문 체크 후 좌표를 queue에 추가
                if building[ni][nj][nk] == "." and not visited[ni][nj][nk]:
                    visited[ni][nj][nk] = 1
                    queue.append((ni, nj, nk, move + 1))

    return "Trapped!"  # while문이 종료됐다면 탈출이 불가하다는 뜻이므로 "Trapped!" return


while True:
    l, r, c = map(int, input().split())
    if not l and not r and not c:
        break

    # 빌딩을 3차원 리스트로 입력받기
    building = []
    for _ in range(l):
        floor = [list(input()) for _ in range(r)]
        building.append(floor)
        input()

    print(bfs())  # bfs
