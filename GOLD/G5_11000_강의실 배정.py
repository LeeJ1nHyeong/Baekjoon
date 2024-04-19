import heapq, sys
input = sys.stdin.readline


n = int(input())
lectures = []  # 강의 시간표를 담을 리스트

# 강의 시간을 튜플 형태로 리스트에 저장
for _ in range(n):
    lectures.append(tuple(map(int, input().split())))

# 시작 시간 순서대로 오름차순 정렬
lectures.sort()

# 가장 빨리 시작하는 강의의 종료시간을 heap에 담은 채로 시작
heap = [lectures[0][1]]

# heap에 있는 가장 작은 종료시간이 다음 강의 시작시간보다 작다면 heappop 진행
for i in range(1, n):
    s, t = lectures[i]
    if heap[0] <= s:
        heapq.heappop(heap)
    # 강의 종료시간을 heappush
    heapq.heappush(heap, t)

print(len(heap))  # heap의 길이 출력
