bracket = input()  # 괄호 문자열
stack = []  # 스택

correct = True  # 올바른 괄호 문자열 판단용

for b in bracket:
    # 여는 괄호('(', '[')라면 stack에 담기
    if b == '(' or b == '[':
        stack.append(b)
    
    # 닫는 소괄호(')')일 경우
    elif b == ')':
        if '(' not in stack:  # stack에 '('가 없다면 for문 종료
            correct = False
            break
        temp = 0  # 숫자 계산용
        while True:
            s = stack.pop()
            if s == '(':  # pop된 문자가 '('라면 계산 후 stack에 담고 while문 종료
                if temp == 0:
                    stack.append(2)
                else:
                    stack.append(2 * temp)
                break
            elif s == '[':  # '['라면 올바른 괄호 문자열이 아니기 때문에 false로 전환 후 while문 종료
                correct = False
                break
            else:  # 나머지의 경우는 숫자밖에 없기 때문에 temp에 숫자 더하기
                temp += s
                
    # 닫는 대괄호(']')일 경우
    elif b == ']':
        if '[' not in stack:  # stack에 '['가 없다면 for문 종료
            correct = False
            break
        temp = 0  # 숫자 계산용
        while True:
            s = stack.pop()
            if s == '[':  # pop된 문자가 '['라면 계산 후 stack에 담고 while문 종료
                if temp == 0:
                    stack.append(3)
                else:
                    stack.append(3 * temp)
                break
            elif s == '(':  # '('라면 올바른 괄호 문자열이 아니기 때문에 false로 전환 후 while문 종료
                correct = False
                break
            else:  # 나머지의 경우는 숫자밖에 없기 때문에 temp에 숫자 더하기
                temp += s

# 올바르지 않은 괄호 문자열일 경우, 혹은 for문 종료 후에도 stack에 괄호가 남아있다면 0으로 출력
if not correct or '(' in stack or '[' in stack:
    ans = 0
else:  # stack내에 남아있는 숫자 합으로 출력
    ans = sum(stack)

print(ans)