def push(x):
    queue.append(x)

def pop():
    if queue:
        print(queue.pop(0))
    else:
        print(-1)

def size():
    print(len(queue))

def empty():
    if queue:
        print(0)
    else:
        print(1)

def front():
    if queue:
        print(queue[0])
    else:
        print(-1)

def back():
    if queue:
        print(queue[-1])
    else:
        print(-1)

import sys
input = sys.stdin.readline

n = int(input())
queue = []

for _ in range(n):
    command = list(map(str, input().split()))
    if command[0] == 'push':
        push(int(command[1]))

    elif command[0] == 'pop':
        pop()

    elif command[0] == 'size':
        size()

    elif command[0] == 'empty':
        empty()

    elif command[0] == 'front':
        front()

    elif command[0] == 'back':
        back()