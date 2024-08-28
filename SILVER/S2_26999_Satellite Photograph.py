'''
문제 설명
- 사진에 찍힌 위성들 중 가장 큰 영역을 가진 위성의 넓이를 출력
'''

from collections import deque

w, h = map(int, input().split())
photo = [list(input()) for _ in range(h)]
visited = [[0] * w for _ in range(h)]

ans = 0
for i in range(h):
    for j in range(w):
        # 빈 공간이거나 방문 지역이라면 continue
        if photo[i][j] == ".":
            continue
        if visited[i][j]:
            continue

        # bfs 초기 세팅
        queue = deque([(i, j)])
        visited[i][j] = 1
        cnt = 1

        # bfs 진행
        while queue:
            ci, cj = queue.popleft()

            for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
                ni, nj = ci + di, cj + dj

                if ni < 0 or ni == h or nj < 0 or nj == w:
                    continue

                if photo[ni][nj] == ".":
                    continue

                if visited[ni][nj]:
                    continue

                # 조건을 충족한 위성 영역이라면 cnt 1 추가, 방문표시, queue에 좌표 추가
                cnt += 1
                visited[ni][nj] = 1
                queue.append((ni, nj))

        # bfs 종료 후 위성 넓이의 최댓값 여부 확인
        ans = max(ans, cnt)

# 위성 넓이의 최댓값 출력
print(ans)
