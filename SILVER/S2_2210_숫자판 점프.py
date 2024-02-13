def dfs(i, j, num):  # dfs
    global cnt
    global num_list

    if len(num) == 6:  # 숫자가 6자리라면 num_list 집합에 숫자를 담고 dfs 종료
        num_list.add(num)
        return
    
    # 5 x 5 숫자판 내에서 6자리가 될 때까지 다음 칸 이동
    for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
        ni, nj = i + di, j + dj
        if 0 <= ni < 5 and 0 <= nj < 5:
            dfs(ni, nj, num + str(board[ni][nj]))


board = [list(map(int, input().split())) for _ in range(5)]
num_list = set()  # 6자리 숫자를 담을 집합

for i in range(5):
    for j in range(5):
        dfs(i, j, f"{board[i][j]}")

print(len(list(num_list)))  # 집합의 크기로 출력