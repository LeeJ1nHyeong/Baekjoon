def recursion(n, start, end):  # 재귀
    mid = 6 - start - end
    if n == 1:  # n == 1일 경우의 예외처리
        from_list.append(start)
        to_list.append(end)
    else:
        recursion(n - 1, start, mid)
        from_list.append(start)
        to_list.append(end)
        recursion(n - 1, mid, end)

n = int(input())

from_list = []  # 시작점 리스트
to_list = []  # 도착점 리스트

recursion(n, 1, 3)  # 1번에서 3번으로 옮기는 것으로 시작

print(2 ** n - 1)  # 호출 횟수에 대한 지수식
for i in range(len(from_list)):
    print(from_list[i], to_list[i])