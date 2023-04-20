import sys
input = sys.stdin.readline

def backtrack(i, part_sum):
    global cnt
    if part_sum == S:
        cnt += 1

    if i == N:
        return

    for j in range(i, N):
        part_sum += num_list[j]
        backtrack(j + 1, part_sum)
        part_sum -= num_list[j]

N, S = map(int, input().split())
num_list = list(map(int, input().split()))
cnt = 0

backtrack(0, 0)

if S == 0:
    print(cnt - 1)
else:
    print(cnt)