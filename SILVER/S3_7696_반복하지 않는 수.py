def make_num(num, visited):  # 수열 제작
    global num_list

    num_list.append(int(num))  # num_list에 수열 추가

    for i in range(10):
        if not visited[i]:  # 사용하지 않은 숫자를 추가한 뒤 백트래킹 진행
            visited[i] = 1
            make_num(num + str(i), visited)
            visited[i] = 0


num_list = [0]  # 인덱스 사용을 편리하게 하기 위해 0을 추가한 상태로 생성
visited = [0] * 10  # 숫자 사용 여부
for i in range(1, 10):
    visited[i] = 1
    make_num(str(i), visited)
    visited[i] = 0

num_list.sort()  # 오름차순 정렬

while True:
    n = int(input())
    if n == 0:  # n이 0이라면 while문 종료
        break

    print(num_list[n])  # 조건에 맞는 n번째 수 츨력
