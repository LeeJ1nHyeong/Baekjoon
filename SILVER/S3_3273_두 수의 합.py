import sys
input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))
num_list.sort()
X = int(input())

cnt = 0

left, right = 0, N - 1

while left < right:
    sum_lr = num_list[left] + num_list[right]
    if sum_lr == X:
        cnt += 1
        left += 1
    elif sum_lr > X:
        right -= 1
    elif sum_lr < X:
        left += 1

print(cnt)