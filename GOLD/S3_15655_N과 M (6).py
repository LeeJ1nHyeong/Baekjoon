def backtrack(cnt, i, lst):  # 백트래킹
    if cnt == m:  # 수열이 M개라면 리스트 내 수열 출력
        print(*lst)
        return

    for j in range(i + 1, n):
        backtrack(cnt + 1, j, lst + [num_list[j]])

n, m = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()  # 오름차순 정렬

backtrack(0, -1, [])  # 백트래킹 진행