import sys
input = sys.stdin.readline

N, S = map(int, input().split())
num_list = list(map(int, input().split()))

l = r = 0
partSum = 0
min_length = 1e5

while True:
    if partSum >= S:
        partSum -= num_list[l]
        l += 1
        min_length = min(min_length, r - l + 1)

    else:
        if r == N:
            break
        else:
            partSum += num_list[r]
            r += 1

if min_length == 1e5:
    print(0)
else:
    print(min_length)