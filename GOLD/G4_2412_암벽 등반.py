from collections import deque


def bfs():
    # bfs 초기 세팅
    queue = deque()
    queue.append((0, 0, 0))

    # bfs 진행
    while queue:
        cx, cy, move = queue.popleft()
        # 목표 높이에 도달했다면 이동 횟수 return
        if cy == T:
            return move
        
        # 좌우 이동거리 절댓값 2 이하, 상하 이동거리 절댓값 2 이하인 좌표 탐색
        for dx in range(-2, 3):
            for dy in range(-2, 3):
                nx, ny = cx + dx, cy + dy

                # 암벽 홈 리스트에 좌표가 없다면 continue
                if (nx, ny) not in groove:
                    continue

                # 있다면 queue에 추가 후 홈 리스트에 좌표 삭제
                queue.append((nx, ny, move + 1))
                groove.remove((nx, ny))

    return -1  # while문이 종료됐다면 목표 지점 이동 불가이므로 -1 return


n, T = map(int, input().split())
groove = set()  # bfs를 진행하기 위해 집합으로 생성

# 홈 좌표를 집합에 추가
for _ in range(n):
    x, y = map(int, input().split())
    groove.add((x, y))

print(bfs())
