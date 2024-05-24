laser = input()
stack = []  # 스택

ans = 0  # 막대기 개수
for i in range(len(laser)):
    l = laser[i]
    # 여는 괄호("(")가 나올 경우 스택에 추가
    if l == "(":
        stack.append(l)
    
    # 닫는 괄호(")")가 나올 경우
    else:
        # 스택에 있는 여는 괄호 하나를 pop
        stack.pop()

        # 이 후 이전 괄호가 여는 괄호일 경우 스택 내의 개수만큼 추가
        if laser[i - 1] == "(":
            ans += len(stack)
        # 닫는 괄호일 경우 1 추가
        else:
            ans += 1

print(ans)  # 막대기 개수 출력
