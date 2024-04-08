import heapq

n = int(input())
heap = []  # 우선순위 큐를 구현할 heap

for _ in range(n):
    number = list(map(int, input().split()))
    for num in number:
        # 메모리 제한으로 인해 heap의 길이를 n으로 제한
        if len(heap) < n:
            heapq.heappush(heap, num)
        else:
            # heap이 다 찼을 경우 현재 숫자가 heap의 최솟값보다 크다면 최솟값을 pop하고 그 숫자를 push
            if num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, num)

print(heap[0])  # heap 내의 최솟값(N번째 큰 수) 출력
