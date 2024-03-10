def backtrack(cnt, i, lst):  # 백트래킹
    if cnt == 6:  # 번호가 6개라면 해당 숫자들 모두 출력
        print(*lst)
        return
    
    # 다음 숫자를 담는 형태로 백트래킹 진행
    for j in range(i + 1, k):
        backtrack(cnt + 1, j, lst + [s[j]])


while True:
    k, *s = map(int, input().split())
    if k == 0:  # k가 0이라면 while문 종료
        break

    # k - 5번째까지 첫 숫자로 백트래킹 시작
    for i in range(k - 5):
        backtrack(1, i, [s[i]])

    print()  # 테스트 케이스별로 공백
