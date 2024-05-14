while True:
    try:
        n = int(input())
        num = "1"

        # num 값이 n으로 나누어 떨어질 때까지 num뒤에 1을 계속 붙이면서 진행
        while True:
            # n으로 나누어 떨어질 경우 num의 길이 출력 후 while문 종료
            if not int(num) % n:
                print(len(num))
                break
            num += "1"

    except:
        break
