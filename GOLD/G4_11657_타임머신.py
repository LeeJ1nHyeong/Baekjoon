def bellman_ford():
    min_time[1] = 0  # 1번 도시의 최단 시간 값을 0으로 변경

    # 각 노선을 n번 순회
    for i in range(n):
        for start, end, time in bus:
            now_time = min_time[start] + time
            if min_time[start] != 1e9 and min_time[end] > now_time:
                min_time[end] = now_time
                # n번째 순회에 값이 갱신된다면 음수 값에 의한 사이클이 있다는 뜻이므로 True return
                if i == n - 1:
                    return True

    return False  # for문이 종료됐다면 음수 값에 의한 사이클이 없다는 뜻이므로 False return


n, m = map(int, input().split())
bus = []  # 버스 노선 정보를 담을 리스트
min_time = [1e9] * (n + 1)  # 각 도시별 최단 시간을 저장할 리스트

# 버스 노선 정보를 리스트에 저장
for _ in range(m):
    a, b, c = map(int, input().split())
    bus.append((a, b, c))

# 벨만-포드 알고리즘을 사용하여 음수 값에 의한 사이클이 존재할 경우 -1 출력
if bellman_ford():
    print(-1)
# 사이클이 없을 경우 1번부터 출발하여 각 도시까지의 최단 시간 값을 출력
else:
    for i in range(2, n + 1):
        # 도착할 수 없다면 -1 출력
        if min_time[i] == 1e9:
            print(-1)
        else:
            print(min_time[i])
