from collections import deque


def bfs():
    # 1000000까지의 방문 여부 표시
    visited = [0] * 1000001
    visited[a] = 1  # 시작 숫자 방문 표시

    queue = deque([(a, 0)])

    # bfs 진행
    while queue:
        num, cnt = queue.popleft()

        # k라면 연산 횟수 return
        if num == k:
            return cnt
        
        # 1000000 이하의 미방문 숫자들에 대해 방문 표시 후 queue에 추가
        if num + 1 <= 1000000 and not visited[num + 1]:
            visited[num + 1] = 1
            queue.append((num + 1, cnt + 1))

        if num * 2 <= 1000000 and not visited[num * 2]:
            visited[num * 2] = 1
            queue.append((num * 2, cnt + 1))


a, k = map(int, input().split())
print(bfs())
