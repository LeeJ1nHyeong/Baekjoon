import sys

N = int(sys.stdin.readline())
stack = []
top = -1

for _ in range(N):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        stack.append(int(command[1]))
        top += 1

    elif command[0] == 'pop':
        if top == -1:
            print(-1)
        else:
            print(stack.pop())
            top -= 1

    elif command[0] == 'size':
        print(len(stack))

    elif command[0] == 'empty':
        if top == -1:
            print(1)
        else:
            print(0)

    elif command[0] == 'top':
        if top == -1:
            print(-1)
        else:
            print(stack[top])