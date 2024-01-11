n = int(input())
num_list = list(map(int, input().split()))
stack = []  # 인덱스를 담을 스택
nge = [-1] * n  # 답안 제출용

for i in range(n):
    # 스택에 담겨있는 맨 위의 인덱스에 해당하는 숫자와 비교
    # i번 인덱스값이 더 높다면 nge의 스택 맨 위 인덱스 값으로 저장
    while stack and num_list[stack[-1]] < num_list[i]:
        idx = stack.pop()
        nge[idx] = num_list[i]
    stack.append(i)

print(*nge)