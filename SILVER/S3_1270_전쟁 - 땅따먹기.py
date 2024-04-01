n = int(input())

for _ in range(n):
    t, *n_t = map(int, input().split())
    number = {}  # 해쉬 구현을 위한 딕셔너리

    ans = "SYJKGW"
    for i in range(t):
        # 딕셔너리 내에 땅 번호가 존재하지 않다면 생성
        if n_t[i] not in number:
            number[n_t[i]] = 1
        # 존재한다면 value 1 추가
        else:
            number[n_t[i]] += 1

        # 해당 번호가 과반수를 넘는다면 ans에 저장 후 for문 종료
        if number[n_t[i]] > t / 2:
            ans = str(n_t[i])
            break

    print(ans)
