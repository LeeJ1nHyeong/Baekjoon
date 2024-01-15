from collections import deque

n, w, l = map(int, input().split())
weight = deque(list(map(int, input().split())))
bridge = deque()  # 다리 위를 큐로 표현
bridge.append(weight.popleft())  # 첫번째 트럭을 다리 위에 미리 올려놓고 시작
over_bridge = []  # 다리를 건넌 트럭

cnt = 1  # 1부터 시작

while True:
    cnt += 1

    if len(bridge) == w:  # 0을 포함해서 다리 큐의 길이가 w라면 가장 왼쪽값을 pop
        now = bridge.popleft()
        if now:
            over_bridge.append(now)  # 0이 아니라면 다리를 건넌 트럭 리스트에 추가

    if len(over_bridge) == n:  # 모든 트럭이 다리를 건넜다면 while문 종료
        break

    # 대기중인 트럭이 없거나 최대하중 초과로 다음 트럭이 건너지 못하면 다리 위의 트럭이 한칸씩 이동하는 뜻으로 0을 추가
    if not weight or sum(bridge) + weight[0] > l:
        bridge.append(0)
    else:
        bridge.append(weight.popleft())  # 다음 트럭이 건널 수 있다면 다음 트럭을 다리 위로 추가

print(cnt)