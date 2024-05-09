import heapq, sys
input = sys.stdin.readline

n = int(input())
lectures = []  # 강의 시간표를 담을 리스트

# 강의 시간표 추가
for _ in range(n):
    num, start, end = map(int, input().split())
    lectures.append((start, end))

lectures.sort()  # 시작 시간을 기준으로 오름차순 정렬

heap = []  # 우선순위 큐
for start, end in lectures:
    # heap이 비어있거나 최솟값이 시작 시간보다 크다면 종료 시간 heappush
    if not heap or heap[0] > start:
        heapq.heappush(heap, end)
    # heap의 최솟값이 시작 시간보다 작거나 같다면 heappop 후 종료 시간 heappush
    elif heap[0] <= start:
        heapq.heappop(heap)
        heapq.heappush(heap, end)

print(len(heap))  # heap의 크기(최소 강의실 수) 출력
