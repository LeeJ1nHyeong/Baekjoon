n, m = map(int, input().split())
numbers = list(map(int, input().split()))
r = [0] * m  # 각 누적합의 나머지를 담을 리스트

# 처음 값부터 i번 인덱스까지의 합을 m으로 나누어 그 나머지 값에 해당하는 인덱스에 1 추가
s = 0
for i in range(n):
    s += numbers[i]
    r[s % m] += 1

cnt = r[0]  # 처음부터 i번 인덱스까지의 합 중 나머지가 0인 값을 cnt에 추가하는 것으로 시작
# 나머지가 같은 두 값을 조합하여 m으로 나누면 나머지가 0
# nC2 값을 cnt에 더해줌
for i in range(m):
    cnt += r[i] * (r[i] - 1) // 2

print(cnt)