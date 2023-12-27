from collections import deque

test_case = int(input())

for _ in range(test_case):
    n, target = map(int, input().split())  # 문서 개수 n, 인쇄 순서를 알고 싶은 문서
    document = list(map(int, input().split()))
    ans = 0
    queue = deque()  # 인덱스를 담기위한 큐 생성
    for i in range(n):
        queue.append(i)

    while True:
        idx = queue.popleft()  # 가장 앞에 있는 문서의 인덱스
        can_print = True  # 프린터 가능 여부
        
        # 나머지 문서 중 중요도 높은 문서가 있는지 확인
        for i in range(len(queue)):
            if document[idx] < document[queue[i]]:
                can_print = False
                break

        if can_print:  # 프린터가 가능하면 프린터 순서 1 증가
            ans += 1
            if idx == target:  # 원하는 문서라면 while문 종료
                break
        else:  # 프린터 불가능하다면 해당 문서의 인덱스를 큐의 맨 뒤로 삽입
            queue.append(idx)

    print(ans)