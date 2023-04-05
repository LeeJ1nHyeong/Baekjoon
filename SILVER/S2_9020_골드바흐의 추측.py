import math
import sys

T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())
    num_list = [i for i in range(n+1)]
    num_list[0], num_list[1] = 0, 0

    for i in range(2, int(math.sqrt(n))+ 1):
        if num_list[i] == i:
            j = 2
            while i * j <= n:
                num_list[i * j] = 0
                j += 1

    for i in range(n+1):
        if num_list[n//2 - i] + num_list[n//2 + i] == n:
            print(num_list[n//2 - i], num_list[n//2 + i])
            break