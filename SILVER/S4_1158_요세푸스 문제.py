from collections import deque

n, k = map(int, input().split())
num_list = [i for i in range(1, n + 1)]  # 1 ~ n번까지의 리스트
queue = deque(num_list)
j = []
idx = 0

# k번째 숫자마다(인덱스 k - 1) 숫자를 요세푸스 리스트(j)에 추가
while queue:
    number = queue.popleft()
    if idx != k - 1:
        queue.append(number)
        idx += 1
    else:
        j.append(number)
        idx = 0

# 출력형식에 맞게 출력
if n == 1:  # n == 1인 경우의 예외처리 추가
    print('<1>')
else:
    for i in range(n):
        if i == 0:
            print(f'<{j[i]},', end=' ')
        elif i == n - 1:
            print(f'{j[i]}>')
        else:
            print(f'{j[i]},', end=' ')