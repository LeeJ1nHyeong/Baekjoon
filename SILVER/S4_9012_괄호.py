T = int(input())

for _ in range(T):
    ps = str(input())
    stack = []
    top = -1
    cnt = 0

    for i in ps:
        if i == '(':
            stack.append(i)
            top += 1

        elif i == ')':
            if top == -1:
                print('NO')
                break
            elif stack[top] == '(':
                stack.pop()
                top -= 1
        cnt += 1
    if cnt == len(ps):
        if len(stack) != 0:
            print('NO')
        else:
            print('YES')