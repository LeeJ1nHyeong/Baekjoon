import heapq

n = int(input())
present = []  # 선물함

for _ in range(n):
    a, *lst = map(int, input().split())

    # a가 0일 경우
    if a == 0:
        # 선물함이 비어있다면 -1 출력
        if not present:
            print(-1)
        # 선물이 있다면 절댓값이 큰 음수값을 양수로 변환하여 출력
        else:
            print(-heapq.heappop(present))
    
    # a가 0이 아닐 경우
    else:
        # 가장 큰 값을 우선순위로 두기 때문에 음수로 변환하여 heappush
        for l in lst:
            heapq.heappush(present, -l)
