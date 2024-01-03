def bfs():  # bfs

    queue = set([])  # 시간초과 방지를 위해 집합 사용
    max_cnt = 0
    queue.add((0, 0, board[0][0]))

    while queue:
        i, j, visited_list = queue.pop()

        max_cnt = max(max_cnt, len(visited_list))

        # 상하좌우 델타 탐색 진행
        for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
            ni, nj = i + di, j + dj
            # visited_list에 탐색 좌표의 알파벳이 없다면
            # 해당 알파벳 추가 후 queue에 추가
            if 0 <= ni < r and 0 <= nj < c and not board[ni][nj] in visited_list:
                queue.add((ni, nj, visited_list + board[ni][nj]))

    return max_cnt

r, c = map(int, input().split())
board = [list(str(input())) for _ in range(r)]

print(bfs())