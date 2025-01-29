n = list(input())

for i in range(len(n)):
    n[i] = int(n[i])

# 숫자에 0이 없거나 숫자 합이 3의 배수가 아니면 30배수를 만들 수 없음
if 0 not in n:
    print(-1)

elif sum(n) % 3:
    print(-1)

else:
    n.sort(reverse=True)

    for i in range(len(n)):
        print(n[i], end="")
