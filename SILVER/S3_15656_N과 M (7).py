def backtrack(cnt, lst):
    if cnt == m:
        print(*lst)
        return

    for i in range(n):
        backtrack(cnt + 1, lst + [num_list[i]])

n, m = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()

backtrack(0, [])