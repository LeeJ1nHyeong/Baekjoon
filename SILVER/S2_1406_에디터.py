# 연결 리스트 활용하여 문제 해결

from collections import deque

word = list(input())
linked1 = deque(word)  # 커서 기준 왼쪽 리스트
linked2 = deque()  # 커서 기준 오른쪽 리스트

m = int(input())

for _ in range(m):
    command = list(map(str, input().split()))
    if command[0] == 'L' and linked1:
        linked2.appendleft(linked1.pop())
    elif command[0] == 'D' and linked2:
        linked1.append(linked2.popleft())
    elif command[0] == 'B' and linked1:
        linked1.pop()
    elif command[0] == 'P':
        linked1.append(command[1])

for l1 in linked1:
    print(l1, end='')
for l2 in linked2:
    print(l2, end='')