from collections import deque


def check():
    num = 1  # 영역 번호
    for i in range(n):
        for j in range(m):
            # 미방문 지역부터 bfs 진행
            if not visited[i][j]:
                visited[i][j] = num
                target1, target2 = flag1[i][j], flag2[i][j]  # 국기 2개를 모두 비교하기 위해 target 변수 2개 생성
                queue = deque([(i, j)])

                # bfs 진행
                while queue:
                    ci, cj = queue.popleft()

                    for d in range(4):
                        ni, nj = ci + di[d], cj + dj[d]
                        if 0 <= ni < n and 0 <= nj < m:
                            # 같은 색깔의 미방문 지역을 탐색
                            if flag1[ni][nj] == target1 and not visited[ni][nj]:
                                # 이 때 2번째 국기도 같은 좌표로 탐색하여 색깔이 다르면 "NO" return 후 bfs 종료
                                if flag2[ni][nj] != target2:
                                    return "NO"
                                # 위 조건 통과 시 해당 위치에 영역 번호 저장 후 queue에 좌표 추가
                                visited[ni][nj] = num
                                queue.append((ni, nj))

                num += 1  # bfs 종료 후 영역 번호 1 증가

    return "YES"  # for문이 종료됐다면 국기를 똑같이 만들 수 있다는 뜻이므로 "YES" return


n, m = map(int, input().split())
flag1 = [list(input()) for _ in range(n)]
flag2 = [list(input()) for _ in range(n)]

visited = [[0] * m for _ in range(n)]  # 방문 여부 확인용 2차원 리스트

# 4방향 델타 탐색
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

print(check())
