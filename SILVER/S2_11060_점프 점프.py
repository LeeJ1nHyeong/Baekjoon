from collections import deque


def bfs():
    visited = [0] * n

    # bfs 초기 세팅
    queue = deque([(0, 0)])  # 시작 위치를 0으로 지정
    visited[0] = 1

    # bfs 진행
    while queue:
        now, move = queue.popleft()

        # 가장 오른쪽 끝에 도착했다면 이동횟수 return
        if now == n - 1:
            return move
        
        # 현재 칸으로부터 칸에 쓰여진 숫자만큼까지 오른쪽 칸들을 탐색
        for i in range(maze[now] + 1):
            next_move = now + i

            if next_move >= n:
                continue

            if visited[next_move]:
                continue

            # 이동 가능한 곳이라면 방문 표시 후 queue에 추가
            visited[next_move] = 1
            queue.append((next_move, move + 1))

    return -1  # while문이 종료됐다면 이동 불가라는 뜻이므로 -1 return


n = int(input())
maze = list(map(int, input().split()))

print(bfs())
