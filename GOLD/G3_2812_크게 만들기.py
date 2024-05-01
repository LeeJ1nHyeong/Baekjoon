n, k = map(int, input().split())
num = input()  # 원활한 분리를 위해 string으로 입력 받기
stack = []  # 숫자를 담을 스택
delete_cnt = 0  # 숫자 제거 횟수

for i in range(n):
    # 숫자 제거 횟수를 넘지 않는 범위에서 현재값보다 작은 값이 나오지 않을 때까지 pop 진행
    while stack and delete_cnt != k and int(stack[-1]) < int(num[i]):
        stack.pop()
        delete_cnt += 1
    # 이 후 stack에 숫자 추가
    stack.append(num[i])

# 숫자 제거 횟수가 k가 아닐 경우 k개가 될 때까지 숫자의 뒷부분을 계속 제거
if delete_cnt != k:
    for _ in range(k - delete_cnt):
        stack.pop()

print("".join(stack))  # k개를 지운 숫자 중 가장 큰 숫자 출력
