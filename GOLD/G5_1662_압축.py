s = input()
stack = []  # 스택
temp = 0  # 문자열 길이 계산을 위한 임시 변수

for i in range(len(s)):
    if s[i] != ")":
        if s[i] == "(":  # 여는 괄호일 경우
            stack.append(temp - 1)  # temp에 1을 뺀 값을 스택에 추가
            stack.append(int(s[i - 1]))  # 여는 괄호 바로 앞의 숫자를 추가
            stack.append(s[i])  # 여는 괄호 추가
            temp = 0  # temp 1로 초기화
        else:  # 숫자일 경우
            temp += 1  # temp 1 추가

    else:  # 닫는 괄호일 경우
        # pop 진행
        while True:
            now = stack.pop()
            if now == "(":  # pop 진행하다가 여는 괄호가 나올 경우
                temp *= stack.pop()  # 다음 pop에 해당하는 숫자를 temp에 곱해서
                stack.append(temp)  # 스택에 추가 후
                break  # while문 종료
            # 숫자라면 temp에 값을 더해주기
            temp += now
        temp = 0  # pop 종료 후 temp 0 초기화

# 모든 과정이 끝나고 temp가 0이 아니라면 스택에 temp값 추가
if temp:
    stack.append(temp)

print(sum(stack))  # 스택에 남아있는 숫자들의 합 출력