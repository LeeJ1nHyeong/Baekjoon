def backtrack(idx, sp, sf, ss, sv, sc, lst):  # 인덱스, 각 영양분의 현재 합, 비용 합, 식재료 리스트
    global minc, n_list
    # 최소 영양분을 모두 만족할 경우에 최소 비용 여부 확인
    if sp >= mp and sf >= mf and ss >= ms and sv >= mv:
        # 최소 비용이라면 최소 비용 및 해당 식재료 리스트 최신화 후 백트래킹 종료
        if minc == -1 or minc > sc:
            minc = sc
            n_list = lst
        return
    
    # 현재 인덱스의 다음 인덱스의 영양분과 비용을 합하고 리스트를 추가한 상태로 백트래킹 진행
    for i in range(idx + 1, n):
        p, f, s, v, c = nutrients[i]
        backtrack(i, sp + p, sf + f, ss + s, sv + v, sc + c, lst + [i + 1])


n = int(input())
mp, mf, ms, mv = map(int, input().split())
nutrients = []  # 영양분 및 비용 리스트

for _ in range(n):
    nutrient = tuple(map(int, input().split()))
    nutrients.append(nutrient)

minc, n_list = -1, []  # 최소 비용, 최소 비용의 식재료 리스트

backtrack(-1, 0, 0, 0, 0, 0, [])  # 백트래킹 진행

# 최소 비용 및 식재료 리스트 출력
print(minc)
print(*n_list)
