n = int(input())
energydrink = sorted(list(map(int, input().split())))  # 에너지 드링크를 오름차순으로 정렬
max_energydrink = energydrink[-1]  # 에너지 드링크의 최댓값으로 시작

# 최댓값 제외한 나머지 에너지 드링크의 절반값을 max_energydrink에 더하기
for e in energydrink[:n - 1]:
    max_energydrink += e / 2

print(max_energydrink)  # 합친 에너지 드링크의 최댓값 출력
