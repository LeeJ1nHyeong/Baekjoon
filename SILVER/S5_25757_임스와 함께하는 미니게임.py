n, game = input().split()
n = int(n)

player = set()

# 게임 참가자 명단을 집합에 저장
for _ in range(n):
    player.add(input())

# 참가자 명단 수를 각 게임별 제한 인원 수로 나눈 몫을 출력
if game == "Y":
    print(len(player))
elif game == "F":
    print(len(player) // 2)
else:
    print(len(player) // 3)
