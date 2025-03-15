from collections import deque

n, m = map(int, input().split())
numbers = list(map(int, input().split()))
queue = deque([i for i in range(1, n + 1)])

ans = 0
for i in range(m):
    target = numbers[i]

    while True:
        if queue[0] == target:
            queue.popleft()
            break

        if queue.index(target) <= len(queue) // 2:
            queue.rotate(-1)
        else:
            queue.rotate(1)

        ans += 1

print(ans)
