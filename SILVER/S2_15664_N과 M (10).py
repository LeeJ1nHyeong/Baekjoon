def backtrack(i, cnt, lst):  # 백트래킹
    global ans

    if cnt == m and lst not in ans:  # 중복 수열을 방지하기 위한 로직
        ans.append(lst)
        return
    
    # 문자열 형태로 수열을 저장한 상태로 백트래킹
    for j in range(i + 1, n):
        backtrack(j, cnt + 1, lst + " " + str(num_list[j]))


n, m = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()  # 오름차순 정렬

ans = []  # 수열을 담을 리스트

for i in range(n):
    backtrack(i, 1, str(num_list[i]))

# 수열 출력
for a in list(ans):
    print(a)