K = int(input())
stack = []
top = -1

for _ in range(K):
    num = int(input())
    if top == -1 or num != 0:
        stack.append(num)
        top += 1
    elif num == 0:
        stack.pop()
        top -= 1

if top == -1:
    print(0)
else:
    print(sum(stack))