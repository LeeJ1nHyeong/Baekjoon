# 연결 리스트 활용하여 문제 해결

from collections import deque

testcase = int(input())

for _ in range(testcase):
    input_list = list(input())
    linked1 = deque()  # 커서 기준 왼쪽 리스트
    linked2 = deque()  # 커서 기준 오른쪽 리스트

    for il in input_list:
        if il == '<':
            if linked1:
                linked2.appendleft(linked1.pop())
        elif il == '>':
            if linked2:
                linked1.append(linked2.popleft())
        elif il == '-':
            if linked1:
                linked1.pop()
        else:
            linked1.append(il)

    for l1 in linked1:
        print(l1, end='')
    for l2 in linked2:
        print(l2, end='')
    print()