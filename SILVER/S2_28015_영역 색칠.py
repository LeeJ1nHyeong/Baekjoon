n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

ans = 0  # 최소 붓질
for i in range(n):
    cnt = 0  # 각 행별 최소 붓질
    target = 0  # 이전 칸의 색
    area1, area2 = 0, 0  # 1의 영역 개수, 2의 영역 개수
    for j in range(m):
        # 현재 칸이 0이라면 두 영역 개수 중 최솟값을 cnt에 더하기
        if board[i][j] == 0:
            cnt += min(area1, area2)
            # 이 때 둘다 0인 경우를 제외하고 cnt에 1을 추가로 더하기
            if area1 or area2:
                cnt += 1
            # 이 후 값 초기화
            target, area1, area2 = 0, 0, 0
        
        # 현재 칸이 0이 아닐 경우
        else:
            # 현재 칸과 이전 칸이 다르다면
            if board[i][j] != target:
                target = board[i][j]  # 이전 칸을 현재칸으로 바꿔줌
                # 현재 칸의 영역 개수를 1 증가
                if board[i][j] == 1:
                    area1 += 1
                else:
                    area2 += 1
            
            # 마지막 열일 경우 두 영역 중 최솟값에 1을 더한 값을 cnt에 더해줌
            if j == m - 1:
                cnt += min(area1, area2) + 1

    # 각 행의 모든 열을 탐색 후 ans에 cnt를 더하기
    ans += cnt

print(ans)