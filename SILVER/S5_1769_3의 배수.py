import sys
input = sys.stdin.readline

x = int(input())
cnt = 0  # 과정 횟수

while True:
    if x < 10:  # 한 자리 수라면 while문 종료
        break

    temp = 0  # 숫자 계산용

    # 두 자리 이상일 경우 각 자리 수를 더하기
    for i in str(x):
        temp += int(i)

    x = temp
    cnt += 1  # 과정 횟수 1 증가

print(cnt)
if x % 3 == 0:
    print("YES")
else:
    print("NO")