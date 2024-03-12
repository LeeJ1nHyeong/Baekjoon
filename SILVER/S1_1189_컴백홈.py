def backtrack(i, j, distance, visited):  # 백트래킹
    global cnt
    # 이동 거리가 k일 때 집에 도착을 했다면 cnt 1 추가
    if distance == k:
        if i == 0 and j == c - 1:
            cnt += 1
        return
    
    # 4방향 탐색하여 백트래킹 진행
    for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
        ni, nj = i + di, j + dj
        if 0 <= ni < r and 0 <= nj < c:
            if board[ni][nj] == "." and not visited[ni][nj]:
                visited[ni][nj] = 1
                backtrack(ni, nj, distance + 1, visited)
                visited[ni][nj] = 0


r, c, k = map(int, input().split())
board = [list(input()) for _ in range(r)]
visited = [[0 for _ in range(c)] for _ in range(r)]  # 방문 여부 체크용 2차원 리스트
cnt = 0  # 거리가 k인 경우의 수

visited[r - 1][0] = 1  # 처음 위치 방문 표시
backtrack(r - 1, 0, 1, visited)  # 백트래킹 진행

print(cnt)
