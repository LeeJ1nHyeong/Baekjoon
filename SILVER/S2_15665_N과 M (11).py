import sys
input = sys.stdin.readline

def backtrack(lst):  # 백트래킹

    if len(lst) == m:  # 수열 길이가 m일 경우 형식에 맞게 수열 출력 후 종료
        print(*lst)
        return

    previous = 0  # 이전 값 저장
    for i in range(n):
        if previous != num_list[i]:  # 수열 중복을 피하기 위해 저장한 이전 값과 비교
            previous = num_list[i]
            backtrack(lst + [num_list[i]])


n, m = map(int, input().split())
num_list = sorted(list(map(int, input().split())))  # 오름차순 정렬한 리스트

backtrack([])  # 빈 리스트로 시작