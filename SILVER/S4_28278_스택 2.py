def push(x):
    stack.append(x)

def pop():
    if stack:
        print(stack.pop(-1))
    else:
        print(-1)

def size():
    print(len(stack))

def empty():
    if not stack:
        print(1)
    else:
        print(0)

def top():
    if stack:
        print(stack[-1])
    else:
        print(-1)

import sys
input = sys.stdin.readline

n = int(input())
stack = []

for _ in range(n):
    command = list(map(int, input().split()))
    if command[0] == 1:
        push(command[1])
    elif command[0] == 2:
        pop()
    elif command[0] == 3:
        size()
    elif command[0] == 4:
        empty()
    elif command[0] == 5:
        top()