import heapq, sys
input = sys.stdin.readline


n = int(input())
cup = []  # 마감일과 컵라면 개수를 저장할 리스트

# 마감일과 컵라면 개수를 튜플 형태로 리스트에 추가 후 마감일 오름차순으로 정렬
for _ in range(n):
    cup.append(tuple(map(int, input().split())))
cup.sort()

heap = []  # 우선순위 큐
for deadline, cnt in cup:
    # 마감일이 heap의 길이보다 클 경우 컵라면 개수를 heappush
    if len(heap) < deadline:
        heapq.heappush(heap, cnt)

    # 마감일이 heap의 길이보다 작거나 같을 경우
    else:
        # 컵라면 개수가 heap 내의 최솟값보다 클 경우 최솟값을 heappop한 후 컵라면 개수를 heappush
        if heap[0] < cnt:
            heapq.heappop(heap)
            heapq.heappush(heap, cnt)

print(sum(heap))  # heap 내의 컵라면 개수 합 출력
