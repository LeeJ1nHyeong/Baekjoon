def check(number):
    for num in number:
        if int(num) != 5 and int(num) != 8:
            return False

    return True


t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))
    k = int(input())
    c = list(map(int, input().split()))

    lucky = set()

    for x in range(n):
        for y in range(m):
            for z in range(k):
                value = a[x] + b[y] + c[z]

                if check(str(value)):
                    lucky.add(value)

    print(len(lucky))
