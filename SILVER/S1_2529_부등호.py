def backtrack(num, visited):  # 백트래킹
    global num_list

    length = len(num)  # 숫자의 길이

    if length == k + 1:  # 숫자 길이가 조건에 만족하면 num_list에 추가 후 백트래킹 종료
        num_list.append(num)
        return
    
    # 조건에 맞게 숫자 추가 진행
    for i in range(10):
        if not visited[i]:
            if not num:
                add_num(i, num, visited)
            else:
                # 다음 부등호가 >일 경우
                if sign[length - 1] == ">" and int(num[-1]) > i:
                    add_num(i, num, visited)
                # 다음 부등호가 <일 경우
                elif sign[length - 1] == "<" and int(num[-1]) < i:
                    add_num(i, num, visited)

# 숫자 추가 후 백트래킹 진행
def add_num(i, num, visited):
    visited[i] = 1
    backtrack(num + str(i), visited)
    visited[i] = 0


k = int(input())
sign = list(input().split())
num_list = []  # 조건에 맞는 숫자를 모을 리스트

backtrack('', [0] * 10)  # 백트래킹

num_list.sort()  # 백트래킹 완료 후 오름차순 정렬
print(num_list[-1])  # 최댓값
print(num_list[0])  # 최솟값
