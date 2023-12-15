def push_front(x):
    deque.insert(0, x)
    return

def push_back(x):
    deque.append(x)
    return

def pop_front():
    if deque:
        print(deque.pop(0))
    else:
        print(-1)

def pop_back():
    if deque:
        print(deque.pop(-1))
    else:
        print(-1)

def size():
    print(len(deque))

def empty():
    if deque:
        print(0)
    else:
        print(1)

def front():
    if deque:
        print(deque[0])
    else:
        print(-1)

def back():
    if deque:
        print(deque[-1])
    else:
        print(-1)

import sys
input = sys.stdin.readline

n = int(input())
deque = []

for _ in range(n):
    command = list(map(str, input().split()))
    if command[0] == 'push_front':
        push_front(int(command[1]))

    elif command[0] == 'push_back':
        push_back(int(command[1]))

    elif command[0] == 'pop_front':
        pop_front()

    elif command[0] == 'pop_back':
        pop_back()

    elif command[0] == 'size':
        size()

    elif command[0] == 'empty':
        empty()

    elif command[0] == 'front':
        front()

    elif command[0] == 'back':
        back()