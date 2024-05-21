def backtrack(lst):
    # 숫자가 모두 들어갔다면 형식에 맞게 출력
    if len(lst) == n:
        print(*lst)
        return
    
    # 리스트 내에 숫자가 없다면 숫자를 리스트에 추가한 형태로 백트래킹 진행
    for i in range(1, n + 1):
        if i not in lst:
            backtrack(lst + [i])


n = int(input())
num = []  # 수열을 담을 리스트

backtrack(num)  # 백트래킹 진행
