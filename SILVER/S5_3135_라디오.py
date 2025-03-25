a, b = map(int, input().split())
n = int(input())
buttons = [int(input()) for _ in range(n)]

ans = abs(a - b)
for button in buttons:
    ans = min(abs(button - b) + 1, ans)

print(ans)
