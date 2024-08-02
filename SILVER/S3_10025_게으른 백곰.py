n, k = map(int, input().split())
basket = []

# 각 얼음 양과 위치를 튜플 형태로 저장
for _ in range(n):
    basket.append(tuple(map(int, input().split())))

# 위치값 오름차순으로 정렬 후 x 최댓값 저장
basket.sort(key=lambda a: a[1])
max_x = basket[-1][1]

# 각 위치 별 얼음 양을 리스트에 저장
ice = [0] * (max_x + 1)
for g, x in basket:
    ice[x] = g

# 0 ~ 2 * k 까지의 얼음 양을 계산
# 최대 거리가 좌우 범위보다 작을 경우에는 최대 거리까지 계산
cnt = 0
for i in range(min(2 * k + 1, max_x + 1)):
    cnt += ice[i]

# 슬라이딩 윈도우를 사용하여 얼음 최댓값 계산
max_cnt = cnt
s, e = 1, min(2 * k + 1, max_x + 1)
while e <= max_x:
    cnt -= ice[s - 1]
    cnt += ice[e]
    max_cnt = max(cnt, max_cnt)
    s += 1
    e += 1

# 얼음 최댓값 계산
print(max_cnt)
