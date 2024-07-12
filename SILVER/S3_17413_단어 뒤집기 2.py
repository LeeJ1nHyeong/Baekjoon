from collections import deque

s = input()
ans = ""
stack = deque()  # 스택

for i in range(len(s)):
    # 오른쪽 부등호일 경우 스택에 담겨있는 문자들을 pop하여 역순으로 ans에 추가 후 스택에 "<" 추가
    if s[i] == "<":
        while stack:
            ans += stack.pop()
        stack.append(s[i])

    # 왼쪽 부등호일 경우 스택에 ">" 추가 후 스택에 담겨 있는 문자 순서 그대로 ans에 추가
    elif s[i] == ">":
        stack.append(s[i])
        while stack:
            ans += stack.popleft()

    # 공백일 경우
    elif s[i] == " ":
        # 스택에 "<"가 있다면 스택에 공백 추가
        if "<" in stack:
            stack.append(" ")
        # 스택에 "<"가 없다면 스택에 담겨있는 문자들을 pop하여 역순으로 ans에 추가 후 ans에 공백 추가
        else:
            while stack:
                ans += stack.pop()
            ans += " "

    # 위 조건 외의 문자들은 스택에 추가
    else:
        stack.append(s[i])

# 문자열 탐색 종료 후 스택에 문자가 남아있다면 역순으로 ans에 추가
if stack:
    while stack:
        ans += stack.pop()

# 뒤집은 문자 출력
print(ans)
