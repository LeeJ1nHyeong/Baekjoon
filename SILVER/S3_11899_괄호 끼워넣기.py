s = input()
ans = 0

stack = []  # 스택

for i in range(len(s)):
    # 여는 괄호 "("가 나올 경우 stack에 추가
    if s[i] == "(":
        stack.append(s[i])

    # 닫는 괄호 ")"가 나올 경우
    else:
        # stack이 비어있다면 ans 1 추가
        if not stack:
            ans += 1
        # stack에 여는 괄호가 들어있다면 pop
        else:
            stack.pop()

# 탐색 완료 후 stack에 남아있는 여는 괄호 수 만큼 ans에 추가
ans += len(stack)

print(ans)
