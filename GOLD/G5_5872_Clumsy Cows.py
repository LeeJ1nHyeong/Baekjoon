'''
짝이 맞지 않은 괄호에 대해 인접 괄호를 뒤집거나 하나를 추가해서 쌍을 맞추기
괄호 뒤집기와 추가한 괄호를 합한 값의 최소 횟수 구하기
'''

parentheses = input()
stack = []

ans = 0
for p in parentheses:
    if p == "(":
        stack.append(p)

    else:
        if not stack:
            ans += 1
            stack.append("(")
        else:
            stack.pop()

ans += len(stack) // 2
print(ans)
