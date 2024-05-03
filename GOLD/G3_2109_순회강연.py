import heapq

n = int(input())
lecture = []  # 강연료와 제한 기간을 담을 리스트

# 강연료와 제한 기간을 lecture에 추가
for _ in range(n):
    p, d = map(int, input().split())
    lecture.append((p, d))

# 제한 기간 오름차순, 강연료 내림차순으로 정렬
lecture.sort(key=lambda x: (x[1], -x[0]))

heap = []  # 우선순위 큐
# 각 강의의 제한 기간을 이용하여 우선순위 큐에 강연료 추기
for p, d in lecture:
    # heap의 크기가 제한 기간보다 작다면 강연료 추가
    if len(heap) < d:
        heapq.heappush(heap, p)

    # heap의 크기가 제한 기간보다 크거나 같을 경우
    else:
        # 강연료가 heap 내의 강연료 중 최솟값보다 클 경우 최솟값 pop 후 강연료 추가
        if p > heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, p)

print(sum(heap))  # heap 내의 강연료 합 출력
