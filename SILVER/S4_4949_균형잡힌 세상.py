while True:
    sentence = str(input())
    stack = []
    top = -1
    cnt = 0

    if sentence == '.':
        break
    else:
        for i in sentence:
            if i == '(' or i == '[':
                stack.append(i)
                top += 1

            elif i == ')':
                if top == -1 or stack[top] != '(':
                    print('no')
                    break
                elif stack[top] == '(':
                    stack.pop()
                    top -= 1

            elif i == ']':
                if top == -1 or stack[top] != '[':
                    print('no')
                    break
                elif stack[top] == '[':
                    stack.pop()
                    top -= 1
            cnt += 1

    if cnt == len(sentence):
        if len(stack) != 0:
            print('no')
        else:
            print('yes')