from collections import deque

n = int(input())
queue = deque([i for i in range(1, n + 1)])
card = []

# queue에 카드가 없을 때까지 진행
while True:
    # 맨 위 카드 제거
    card.append(queue.popleft())

    if not queue:
        break

    # 다음 맨 위 카드를 맨 아래로 이동
    queue.append(queue.popleft())

print(*card)
