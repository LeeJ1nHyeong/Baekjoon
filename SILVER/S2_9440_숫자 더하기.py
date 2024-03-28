import math

while True:
    n, *num = map(int, input().split())  # 숫자 개수, 숫자 목록
    if n == 0:  # n이 0일 경우 while문 종료
        break

    num.sort()  # 오름차순 정렬

    # 0 개수 세기
    zero_cnt = 0
    for i in range(n):
        if num[i] == 0:
            zero_cnt += 1

    number1, number2 = 0, 0  # 조합하여 만들 숫자 2개

    # 0이 없을 경우
    if not zero_cnt:
        # n이 홀수일 경우 number1의 자리수를 하나 더 많게 설정
        if n % 2:
            number1 = num[0] * 10 + num[1]  # 가장 작은 두 숫자를 number1에 배치
            number2 = num[2]  # 다음 숫자 1개를 number2에 배치

            # 이 후 1개씩 번갈아가며 숫자 추가
            for i in range(3, n):
                if i % 2:
                    number1 = number1 * 10 + num[i]
                else:
                    number2 = number2 * 10 + num[i]
        
        # n이 짝수일 경우
        else:
            # 가장 작은 두 숫자를 각각 1개씩 배치
            number1 = num[0]
            number2 = num[1]

            # 이 후 1개씩 번갈아가며 숫자 추가
            for i in range(2, n):
                if i % 2 == 0:
                    number1 = number1 * 10 + num[i]
                else:
                    number2 = number2 * 10 + num[i]

    # 0이 존재할 경우
    else:
        # 0 제외 가장 작은 두 숫자를 각각 1개씩 배치
        number1, number2 = num[zero_cnt], num[zero_cnt + 1]

        # 0 개수가 홀수일 경우 number1에 1개 더 많게 0 추가
        number1 *= 10 ** math.ceil(zero_cnt / 2)
        number2 *= 10 ** math.floor(zero_cnt / 2)

        # 이 후 1개씩 번갈아가며 숫자 추가
        for i in range(zero_cnt + 2, n):
            if i % 2 == 0:
                number1 = number1 * 10 + num[i]
            else:
                number2 = number2 * 10 + num[i]

    print(number1 + number2)  # 두 수의 합의 최솟값 출력
