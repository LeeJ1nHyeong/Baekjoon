import sys
from collections import deque
input = sys.stdin.readline

A, B = map(int, input().split())

queue = deque()
queue.append((A, 1))

ans = -1

while queue:
    a, cnt = queue.popleft()

    if a * 2 == B or int(str(a) + '1') == B:
        ans = cnt + 1
        break
    else:
        if a * 2 < B:
            queue.append((a * 2, cnt + 1))
        if int(str(a) + '1') < B:
            queue.append((int(str(a) + '1'), cnt + 1))

print(ans)