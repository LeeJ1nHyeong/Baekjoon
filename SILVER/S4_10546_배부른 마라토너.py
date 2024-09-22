import sys
input = sys.stdin.readline

n = int(input())
marathoner = {}

# 마라토너 명단에 이름 추가
for _ in range(n):
    name = input()

    if name not in marathoner:
        marathoner[name] = 1

    # 동명이인도 있을 수 있기 때문에 이름이 존재한다면 해당 key의 value를 1 추가
    else:
        marathoner[name] += 1

# 이 후 완주자의 이름에 해당하는 value 1 감소
for _ in range(n - 1):
    name = input()
    marathoner[name] -= 1

# 마라토너 이름으로 해시를 탐색하여 value가 1인 이름을 출력
for name in marathoner.keys():
    if marathoner[name]:
        print(name)
        break
