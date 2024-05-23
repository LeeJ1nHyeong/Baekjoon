import heapq

n = int(input())
homeworks = []  # 과제 마감일과 점수를 저장할 리스트

# 과제 마감일과 점수를 튜플 형태로 리스트에 저장
for _ in range(n):
    homeworks.append(tuple(map(int, input().split())))

# 과제 마감일 오름차순, 같다면 점수 내림차순으로 정렬
homeworks.sort(key=lambda x: (x[0], -x[1]))

heap = []  # 우선순위 큐
for d, w in homeworks:
    # 마감일이 heap의 길이보다 클 경우 점수를 heap에 heappush
    if len(heap) < d:
        heapq.heappush(heap, w)
    
    # 마감일이 heap의 길이보다 작거나 같을 경우, heap 내의 점수 최솟값을 비교
    else:
        # 점수가 heap 내 점수 최솟값보다 클 경우 최솟값을 heappop 후 점수 heappush
        if w > heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, w)

print(sum(heap))  # heap 내의 점수 합 출력
