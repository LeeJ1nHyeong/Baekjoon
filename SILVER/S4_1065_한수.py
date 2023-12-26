n = int(input())  # n < 1000인 자연수
cnt = 0

for i in range(1, n + 1):
    if i < 10:  # 한 자리 수
        cnt += 1

    elif i >= 10 and i < 100:  # 두 자리 수
        cnt += 1

    elif i >= 100:  # 세 자리 수
        a = i // 100
        b = (i // 10) % 10
        c = i % 10
        if (a - b) == (b - c):
            cnt += 1

print(cnt)