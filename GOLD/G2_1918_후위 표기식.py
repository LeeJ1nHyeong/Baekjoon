import sys

expression = str(sys.stdin.readline())
stack = []
calculator = []

for i in expression:
    if i.isalpha():
        calculator.append(i)
        if len(stack):
            a = stack.pop()
            if a == '*' or a == '/':
                calculator.append(a)
            else:
                stack.append(a)

    elif i == '(':
        stack.append(i)

    elif i == ')':
        while stack:
            a = stack.pop()
            if a == '(':
                break
            else:
                calculator.append(a)

        while stack:
            b = stack.pop()
            if b == '*' or b == '/':
                calculator.append(b)
            else:
                stack.append(b)
                break

    elif i == '+' or i == '-':
        if len(stack):
            while stack:
                a = stack.pop()
                if a == '(':
                    stack.append(a)
                    break
                else:
                    calculator.append(a)
        stack.append(i)

    elif i == '*' or i == '/':
        stack.append(i)


while stack:
    calculator.append(stack.pop())

for c in calculator:
    print(c, end='')