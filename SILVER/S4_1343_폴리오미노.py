## 풀이 1
def polyomino():
    cnt = 0
    for i in range(len(board)):
        # "."이 나왔을 경우
        if board[i] == ".":
            # 연속 X개수가 홀수라면 -1 return
            if cnt % 2 == 1:
                return -1
            # 연속 X개수가 2개라면 그 자리를 B로 채우고 0으로 초기화
            if cnt == 2:
                for j in range(i - 2, i):
                    board[j] = "B"
                cnt = 0

        # "X"가 나올 경우
        else:
            # 연속 X개수 1 추가
            cnt += 1
            # 연속 X개수가 4개라면 그 자리를 A로 채우고 0으로 초기화
            if cnt == 4:
                for j in range(i - 3, i + 1):
                    board[j] = "A"
                cnt = 0

    # 탐색 종료 후 cnt가 홀수라면 1 return
    if cnt % 2 == 1:
        return -1
    
    # cnt가 2라면 맨 뒤의 2칸을 B로 교체
    if cnt == 2:
        board[-2], board[-1] = "B", "B"

    # 형식에 맞게 return
    ans = "".join(board)
    return ans


board = list(input())

print(polyomino())


## 풀이 2
board = input()

# X가 4개 연속으로 붙어있는 구간을 A로 교체
board = board.replace("XXXX", "AAAA")
# 이 후 2개 연속ㅇ로 붙어있는 구간을 B로 교체
board = board.replace("XX", "BB")

# 위 과정 진행 후에도 X가 남아있다면 -1 출력
if "X" in board:
    print(-1)
# X가 없다면 교체된 상태로 출력 
else:
    print(board)