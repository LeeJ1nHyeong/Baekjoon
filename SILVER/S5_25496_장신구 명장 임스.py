p, n = map(int, input().split())
# 피로도를 오름차순 정렬한 상태로 저장
fatigue = sorted(list(map(int, input().split())))

ans = 0  # 만들 수 있는 장신구 개수
for i in range(n):
    # 피로도가 200 이상이 될 경우 break
    if p >= 200:
        break

    # 피로도를 누적시키고 장신구 개수 1 추가
    p += fatigue[i]
    ans += 1

# 만들 수 있는 장신구 개수 출력
print(ans)
