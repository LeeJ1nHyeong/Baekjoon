n, m = map(int, input().split())
apart = [0] * 10001  # 최대 10000층

# 참가자 번호를 해당 층에 저장
for num in range(1, m + 1):
    h1, h2 = map(int, input().split())
    apart[h1 - 1] = num
    apart[h2 - 1] = num

# 값이 존재하는 층만 filter로 따로 저장
filter_apart = list(filter(lambda x: x > 0, apart))

# n층인 참가자 번호 저장
print(filter_apart[n % (2 * m) - 1])
