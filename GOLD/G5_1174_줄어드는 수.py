def backtrack(i, num):
    if num:  # 백트래킹으로 생성된 숫자를 리스트에 추가
        num_list.append(int(num))

    # i부터 역순으로 for문을 사용하여 백트래킹
    for j in range(i, -1, -1):
        backtrack(j - 1, num + str(j))


n = int(input())

num_list = []  # 줄어드는 수를 담을 리스트

# 백트래킹으로 줄어드는 수 리스트 만들고 오름차순
backtrack(9, "")
num_list.sort()

# 줄어드는 수의 개수는 한정적이기 때문에 n이 리스트 길이보다 크다면 -1 출력, 작다면 해당 값 출력
if n > len(num_list):
    print(-1)
else:
    print(num_list[n - 1])