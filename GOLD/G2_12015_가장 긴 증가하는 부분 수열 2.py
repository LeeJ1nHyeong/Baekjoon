def binary_search(start, end, target):  # 이진 탐색
    # start가 end보다 크거나 같다면 증가 수열의 end index를 target 값으로 변경 후 종료
    if start >= end:
        increase_list[end] = target
        return
    
    # 이진 탐색 진행
    mid = (start + end) // 2

    if increase_list[mid] < target:
        return binary_search(mid + 1, end, target)
    else:
        return binary_search(start, mid, target)

n = int(input())
num_list = list(map(int, input().split()))

increase_list = [num_list[0]]  # 증가 부분 수열을 담을 리스트

for i in range(1, n):
    # i번 index 값이 현재 증가 부분 수열의 마지막 수보다 크다면 증가 부분 수열 리스트에 담기
    if num_list[i] > increase_list[-1]:
        increase_list.append(num_list[i])
    # 그렇지 않다면 이진 탐색을 진행하여 적절한 위치에 해당 값을 변환
    elif num_list[i] < increase_list[-1]:
        binary_search(0, len(increase_list) - 1, num_list[i])

print(len(increase_list))  # 가장 긴 증가 부분 수열의 길이 출력