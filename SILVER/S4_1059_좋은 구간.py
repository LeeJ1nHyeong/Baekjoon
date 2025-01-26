l = int(input())
s = list(map(int, input().split()))
n = int(input())

s.sort()

if n in s:
    print(0)
else:
    min_value, max_value = 0, 0

    for num in s:
        if num < n:
            min_value = num
        elif num > n and max_value == 0:
            max_value = num

    max_value -= 1
    min_value += 1

    ans = (n - min_value) * (max_value - n + 1) + (max_value - n)
    print(ans)
