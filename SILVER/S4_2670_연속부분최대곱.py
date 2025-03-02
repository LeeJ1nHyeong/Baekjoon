n = int(input())
numbers = [float(input()) for _ in range(n)]

for i in range(1, n):
    numbers[i] = max(numbers[i], numbers[i - 1] * numbers[i])

# round를 사용하면 오사오입으로 일부 틀린 답이 나올 수 있으므로 % 서식을 활용
print("%.3f" % max(numbers))
