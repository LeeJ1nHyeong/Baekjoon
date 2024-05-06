def bellman_ford():
    min_time = [1e9] * (n + 1)  # 각 지점까지의 최단 시간을 저장할 리스트
    min_time[1] = 0  # 시작 지점을 아무 곳이나 하나 선점(1번 지점)

    # 도로 및 웜홀을 n번 순회
    for i in range(n):
        for start, end, time in nodes:
            if min_time[end] > min_time[start] + time:
                min_time[end] = min_time[start] + time
                # n번째 순회에서 최단 시간 값이 갱신이 된다면 음수값이 존재하여 사이클이 존재한다는 뜻
                if i == n - 1:
                    return "YES"  # "YES" return

    return "NO"  # for문이 종료될 경우 음수값이 없다는 뜻이므로 "NO" return


tc = int(input())

for _ in range(tc):
    n, m, w = map(int, input().split())
    nodes = []  # 지점 간의 도로 및 웜홀 정보를 담을 리스트

    # 도로 정보를 리스트에 추가
    for _ in range(m):
        s, e, t = map(int, input().split())
        nodes.append((s, e, t))
        nodes.append((e, s, t))

    # 웜홀 정보를 리스트에 추가
    for _ in range(w):
        s, e, t = map(int, input().split())
        nodes.append((s, e, -t))

    print(bellman_ford())  # 벨만-포드 알고리즘으로 탐색
