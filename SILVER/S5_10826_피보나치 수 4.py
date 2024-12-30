n = int(input())
if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    fibonacci = [0] * (n + 1)
    fibonacci[1] = 1

    for i in range(2, n + 1):
        fibonacci[i] = fibonacci[i - 1] + fibonacci[i - 2]

    print(fibonacci[n])
