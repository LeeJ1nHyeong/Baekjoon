import math

M, N = map(int, input().split())

num_list = [True for _ in range(N + 1)] # 모든 리스트가 소수(True)인
num_list[0] = False
num_list[1] = False

for i in range(2, int(math.sqrt(N)) + 1):
    if num_list[i] == True:
        j = 2
        while i * j <= N:
            num_list[i * j] = False
            j += 1

for i in range(M, N+1):
    if num_list[i] == True:
        print(i)