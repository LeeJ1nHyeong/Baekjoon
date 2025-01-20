import sys
input = sys.stdin.readline

n = int(input())
if n == 0:
    print(0)

else:
    difficulty = [int(input()) for _ in range(n)]
    difficulty.sort()

    # python의 round 함수는 오사오입이 적용되어있기 때문에 반올림할 값에 0.00001을 더해서 오답 방지
    cut = round(n * 0.15 + 0.00001)
    if cut:
        print(round(sum(difficulty[cut:-cut]) / len(difficulty[cut:-cut]) + 0.00001))
    else:
        print(round(sum(difficulty) / len(difficulty) + 0.00001))
