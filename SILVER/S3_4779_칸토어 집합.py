def divide_and_conquer(n):
    # n이 1일 경우 "-" 하나만 return
    if n == 1:
        return "-"
    
    # 3등분으로 만들기
    unit = divide_and_conquer(n // 3)

    # 3등분 중 두 조각을 양 끝에 배치 후 가운데 공백을 (n // 3)칸 만큼 추가
    whole = unit + " " * (n // 3) + unit

    return whole


while True:
    try:
        n = int(input())
        print(divide_and_conquer(3 ** n))  # 분할정복 진행

    except:
        break
