p, m = map(int, input().split())
rooms = []

for _ in range(p):
    l, n = input().split()

    is_join = False  # 현재 참가자의 방 입장 여부

    # 입장 가능한 방 탐색
    for room in rooms:
        if len(room) == m:
            continue

        if not room or abs(room[0][0] - int(l)) <= 10:
            room.append((int(l), n))
            is_join = True
            break

    # 입장하지 못했다면 방 새로 생성
    if not is_join:
        rooms.append([(int(l), n)])

for room in rooms:
    # 참가자 닉네임 오름차순 정렬
    room.sort(key=lambda x: x[1])

    print("Started!" if len(room) == m else "Waiting!")

    for player in room:
        print(*player)
