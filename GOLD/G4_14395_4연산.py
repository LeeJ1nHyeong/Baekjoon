from collections import deque


def bfs():
    # 연산 전 s와 t가 같다면 0을 return
    if s == t:
        return 0

    queue = deque([(s, "")])
    visited = set()
    visited.add(s)

    while queue:
        now, calculator = queue.popleft()

        if now == t:
            return calculator
        
        # 최소 연산 횟수를 구하기 때문에 빼기 연산은 필요가 없어서 제외
        if now ** 2 <= 10 ** 9 and now ** 2 not in visited:
            visited.add(now ** 2)
            queue.append((now ** 2, calculator + "*"))

        if now * 2 <= 10 ** 9 and now * 2 not in visited:
            visited.add(now * 2)
            queue.append((now * 2, calculator + "+"))

        if now / now not in visited:
            visited.add(now / now)
            queue.append((now / now, calculator + "/"))

    return -1  # s를 t로 바꿀 수 없다면 -1 return


s, t = map(int, input().split())

print(bfs())
