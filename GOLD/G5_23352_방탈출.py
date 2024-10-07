from collections import deque


def bfs(si, sj):
    global max_move, max_password

    # bfs 초기 세팅
    visited = [[0] * m for _ in range(n)]  # 시작 지점이 매번 바뀌기 때문에 방문 표시 리스트도 매번 생성
    queue = deque([(si, sj, 1)])
    visited[si][sj] = 1

    # bfs 진행
    while queue:
        ci, cj, move = queue.popleft()

        # 시작점과 끝점을 합한 값을 비밀번호로 저장
        password = board[si][sj] + board[ci][cj]

        # 최대 이동횟수일 경우 이동횟수와 비밀번호 최신화
        if move > max_move:
            max_move = move
            max_password = password

        # 현재 이동횟수가 최대 이동횟수와 같을 경우 비밀번호 최댓값 여부 확인
        elif move == max_move:
            max_password = max(password, max_password)

        # 상하좌우 4방향 탐색
        for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
            ni, nj = ci + di, cj + dj

            if ni < 0 or ni == n or nj < 0 or nj == m:
                continue

            if not board[ni][nj]:
                continue

            if visited[ni][nj]:
                continue

            # 이동 가능한 좌표에 대해 방문 표시 후 queue에 좌표 추가
            visited[ni][nj] = 1
            queue.append((ni, nj, move + 1))


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

max_move = 0  # 가장 긴 경로
max_password = 0  # 가장 긴 경로에서의 비밀번호 최댓값

# 빈 방을 제외한 곳을 시작점으로 지정하여 탐색
for i in range(n):
    for j in range(m):
        if not board[i][j]:
            continue

        bfs(i, j)

print(max_password)  # 비밀번호 최댓값 출력
