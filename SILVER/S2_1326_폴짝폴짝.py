from collections import deque


def bfs():
    queue = deque([(a, 0)])
    visited[a] = 1

    while queue:
        now, cnt = queue.popleft()

        if now == b:
            return cnt

        # 현재 위치의 뒤로 이동
        prev_move = now
        while True:
            prev_move -= bridge[now]
            if prev_move <= 0:
                break

            if visited[prev_move]:
                continue

            visited[prev_move] = 1
            queue.append((prev_move, cnt + 1))

        # 현재 위치의 앞으로 이동
        next_move = now
        while True:
            next_move += bridge[now]
            if next_move > n:
                break

            if visited[next_move]:
                continue

            visited[next_move] = 1
            queue.append((next_move, cnt + 1))

    return -1


n = int(input())
bridge = [0] + list(map(int, input().split()))
a, b = map(int, input().split())
visited = [0] * (n + 1)

print(bfs())
