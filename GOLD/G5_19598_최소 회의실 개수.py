import heapq

n = int(input())
meetings = []  # 회의 시작 시간과 종료 시간을 저장할 리스트

# 회의 시작 시간과 종료 시간을 튜플 형태로 저장
for _ in range(n):
    meetings.append(tuple(map(int, input().split())))

meetings.sort()  # 오름차순 정렬

heap = []  # 우선순위 큐

for start, end in meetings:
    # heap이 비어있거나 heap 내의 가장 빠른 종료 시간이 현재의 시작 시간보다 클 경우 종료 시간 heappush
    if not heap or heap[0] > start:
        heapq.heappush(heap, end)

    # heap 내의 가장 빠른 종료 시간이 현재의 시작 시간보다 작거나 같을 경우 heappop 후 종료 시간 heappush
    elif heap[0] <= start:
        heapq.heappop(heap)
        heapq.heappush(heap, end)

print(len(heap))  # heap 크기 출력
