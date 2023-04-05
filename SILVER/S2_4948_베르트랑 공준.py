import math
import sys

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break

    else:
        num_list = [True for _ in range(2*n + 1)]
        num_list[0], num_list[1] = False, False

        for i in range(2, int(math.sqrt(2*n))+1):
            if num_list[i] == True:
                j = 2
                while i * j <= 2*n:
                    num_list[i * j] = False
                    j += 1

        cnt = 0
        for i in range(n + 1, 2 * n + 1):
            if num_list[i] == True:
                cnt += 1

        print(cnt)