x, y, w, s = map(int, input().split())

if x == 0 or y == 0:  # x 또는 y에 0이 있을 경우
    if x == 0:
        if y % 2:
            print(min((y - 1) * s + w, y * w))
        else:
            print(min(y * w, y * s))
    else:
        if x % 2:
            print(min((x - 1) * s + w, x * w))
        else:
            print(min(x * w, x * s))

else:
    if w * 2 < s:  # 직선 2회가 대각선보다 더 빠를 경우
        print((x + y) * w)
    elif w >= s:  # 대각선이 더 빠를 경우
        if (x + y) % 2:
            print((max(x, y) - 1) * s + w)
        else:
            print(max(x, y) * s)
    else:  # w < s <= 2 * w일 경우
        print((min(x, y) * s + abs(x - y) * w))