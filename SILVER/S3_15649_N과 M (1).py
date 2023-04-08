def backtrack():
    if len(num_list) == M:
        for i in num_list:
            print(i, end=' ')
        print()

    for i in range(1, N+1):
        if i not in num_list:
            num_list.append(i)
            backtrack()
            num_list.pop()

N, M = map(int, input().split())
num_list = []

backtrack()