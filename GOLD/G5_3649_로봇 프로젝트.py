def two_pointer():
    left, right = 0, n - 1

    while left < right:
        sum_left = lego[left] + lego[right]
        # 두 수의 합이 목표값에 도달할 경우 출력 형식에 맞게 return
        if sum_left == x:
            return f"yes {lego[left]} {lego[right]}"
        # 두 수의 합이 목표값보다 클 경우 오른쪽 포인터 1 감소
        elif sum_left > x:
            right -= 1
        # 두 수의 합이 목표값보다 클 경우 왼쪽 포인터 1 증가
        elif sum_left < x:
            left += 1

    return "danger"  # while문 종료됐을 경우 목표값을 찾지 못했다는 뜻이므로 "danger" return


while True:
    try:
        x = int(input()) * 10000000  # 구멍의 너비를 나노미터 단위 형태로 변환
        lego = []
        n = int(input())
        # 레고 조각 크기를 리스트에 추가
        for _ in range(n):
            l = int(input())
            lego.append(l)

        lego.sort()  # 레고 조각 크기 오름차순 정렬

        print(two_pointer())  # 투 포인터 진행

    except:
        break
