import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    P = str(input())
    N = int(input())
    num_list = input().rstrip()[1:-1].split(',')
    queue = deque(num_list)
    reverse_cnt = 0
    error = False

    if N == 0:
        queue = []

    for p in P:
        if p == 'R':
            reverse_cnt += 1

        elif p == 'D':
            if not queue:
                error = True
                print('error')
                break
            else:
                if reverse_cnt % 2:
                    queue.pop()
                else:
                    queue.popleft()

    if not error:
        if reverse_cnt % 2:
            queue.reverse()
        print('[%s]' % ','.join(queue))