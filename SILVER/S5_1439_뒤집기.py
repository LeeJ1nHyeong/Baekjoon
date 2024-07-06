s = input()
reverse = [0, 0]  # 각 숫자로 연속된 묶음을 뒤집을 횟수
reverse[int(s[0])] = 1  # 첫번째 숫자에 대해 1 추가

# 현재 숫자가 이전 숫자와 다르다면 현재 숫자에 대해 1 추가
for i in range(1, len(s)):
    if s[i] != s[i - 1]:
        reverse[int(s[i])] += 1

print(min(reverse))  # 두 수 중 최솟값을 출력
