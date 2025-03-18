n = int(input())
numbers = list(map(int, input().split()))
stack = []

now = 1
for i in range(n):
    stack.append(numbers[i])

    while stack and stack[-1] == now:
        stack.pop()
        now += 1

print("Nice" if not stack else "Sad")
