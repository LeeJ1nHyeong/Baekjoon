import sys
input = sys.stdin.readline

def two_pointer(i, left, right):
    global a, b, c
    global min_solution

    while left != right:
        if i + num_list[left] + num_list[right] == 0:
            a, b, c = i, num_list[left], num_list[right]
            return

        if abs(i + num_list[left] + num_list[right]) < min_solution:
            a, b, c = i, num_list[left], num_list[right]
            min_solution = abs(i + num_list[left] + num_list[right])

        if i + num_list[left] + num_list[right] < 0:
            left += 1
        elif i + num_list[left] + num_list[right] > 0:
            right -= 1

N = int(input())
num_list = list(map(int, input().split()))
num_list.sort()
a, b, c = 0, 0, 0
min_solution = 1e10

for i in range(N - 1):
    two_pointer(num_list[i], i + 1, N - 1)

print(a, b, c)