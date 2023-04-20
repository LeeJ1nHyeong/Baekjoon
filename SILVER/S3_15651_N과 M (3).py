import sys
input = sys.stdin.readline

def backtrack(cnt):
    global num_list
    if cnt == M:
        print(*num_list)
        return

    for i in range(1, N + 1):
        num_list.append(i)
        backtrack(cnt + 1)
        num_list.pop()

N, M = map(int, input().split())
num_list = []

backtrack(0)