import sys
input = sys.stdin.readline

def two_pointer(left, right):
    global a, b
    global sub

    while left != right:
        if num_list[left] == - num_list[right]:
            a, b = num_list[left], num_list[right]
            return

        if sub > abs(num_list[left] + num_list[right]):
            sub = abs(num_list[left] + num_list[right])
            a, b = num_list[left], num_list[right]

        if num_list[left] + num_list[right] < 0:
            left += 1
        elif num_list[left] + num_list[right] > 0:
            right -= 1

N = int(input())
num_list = list(map(int, input().split()))
a, b = 0, 0
sub = 1e10

two_pointer(0, N - 1)

print(a, b)