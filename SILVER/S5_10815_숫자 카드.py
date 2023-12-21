def binarySearch(low, high, key):  # 이진 탐색
    if low > high:
        return 0

    mid = (low + high) // 2
    if key == N_list[mid]:
        return 1
    elif key < N_list[mid]:
        return binarySearch(low, mid - 1, key)
    elif key > N_list[mid]:
        return binarySearch(mid + 1, high, key)

import sys
input = sys.stdin.readline

N = int(input())
N_list = list(map(int,input().split()))
N_list.sort()
M = int(input())
M_list = list(map(int,input().split()))

# M_list의 숫자가 N_list 안에 있는지 표시하는 용도
seek = [0 for _ in range(M)]

for i in range(M):
    seek[i] = binarySearch(0, N - 1, M_list[i])

print(*seek)