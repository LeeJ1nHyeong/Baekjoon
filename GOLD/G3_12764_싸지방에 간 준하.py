import heapq


n = int(input())

# 싸지방 이용 시작 시간과 종료 시간을 튜플 형태로 저장
user = []
for _ in range(n):
    user.append(tuple(map(int, input().split())))

# 시작 시간 오름차순으로 정렬
user.sort()

end_heap = []  # 종료 시간과 컴퓨터 번호를 저장할 우선순위 큐
empty_computer_heap = []  # 비어있는 컴퓨터 번호를 저장할 우선순위 큐
computer_used = [0] * 100000  # 컴퓨터 사용 횟수

x = 0  # 필요한 최소 컴퓨터 수
for p, q in user:
    # end_heap이 비어있거나 시작 시간이 end_heap 내의 종료 시간 최솟값보다 작을 경우
    if not end_heap or end_heap[0][0] > p:
        # 비어있는 컴퓨터가 있으면 가장 작은 번호를 선택
        if empty_computer_heap:
            num = heapq.heappop(empty_computer_heap)
            computer_used[num] += 1
            heapq.heappush(end_heap, (q, num))

        # 비어있는 컴퓨터가 없으면 x를 선택 후 x 1 증가
        else:
            heapq.heappush(end_heap, (q, x))
            computer_used[x] += 1
            x += 1

    # 시작 시간이 end_heap 내의 종료 시간 최솟값보다 클 경우
    elif end_heap[0][0] < p:
        # end_heap 내에 있는 종료 시간이 시작 시간보다 작은 값들은 모두 pop  
        while True:
            # end_heap이 비었거나 종료 시간이 더 큰 값이 나올 경우
            if not end_heap or end_heap[0][0] > p:
                # 비어있는 컴퓨터 목록에서 가장 작은 번호를 선택하여 end_heap에 추가
                num = heapq.heappop(empty_computer_heap)
                heapq.heappush(end_heap, (q, num))
                computer_used[num] += 1
                break

            # pop 진행하면서 컴퓨터 번호는 empty_computer_heap에 저장
            end_time, num = heapq.heappop(end_heap)
            heapq.heappush(empty_computer_heap, num)

# 최소 컴퓨터 개수와 각 자리 별 사용 횟수 출력
print(x)
print(*computer_used[:x])
