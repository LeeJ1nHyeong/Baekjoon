v, e = map(int, input().split())
routes = [[10001 * v] * (v + 1) for _ in range(v + 1)]  # 마을 간의 최소 길이를 구하기 위한 2차원 리스트

# 각 마을 간의 도로 길이 저장
for _ in range(e):
    a, b, c = map(int, input().split())
    routes[a][b] = c

# 각 마을까지의 도로 길이와 k번 마을을 중간 지점으로 방문 후 도착했을 때의 길이를 비교하여 최솟값을 저장
min_dist = 10001 * v
for k in range(1, v + 1):
    for i in range(1, v + 1):
        for j in range(1, v + 1):
            routes[i][j] = min(routes[i][j], routes[i][k] + routes[k][j])

# 사이클이 형성된 값을 비교하여 최솟값 저장
for i in range(1, v + 1):
    min_dist = min(min_dist, routes[i][i])

# 도로 길이 최솟값이 처음 값 그대로라면 -1 출력, 값이 바뀌었다면 해당 값 출력
if min_dist == 10001 * v:
    print(-1)
else:
    print(min_dist)