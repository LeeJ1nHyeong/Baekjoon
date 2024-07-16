n, s, r = map(int, input().split())
broken = set(map(int, input().split()))
extra = set(map(int, input().split()))

both = broken & extra  # 카약이 망가졌지만 여분을 더 들고온 팀
broken = list(broken - both)  # 카약이 망가진 팀
extra = list(extra - both)  # 여분이 있는 팀

ans = 0  # 카약을 못 빌린 팀
# 카약이 망가진 팀 탐색
for b in broken:
    # 앞 뒤 팀 중에 여분이 있는 팀이 있다면 extra에서 그 팀 제거
    if b - 1 in extra:
        extra.remove(b - 1)
    elif b + 1 in extra:
        extra.remove(b + 1)
    # 둘 다 여분이 없다면 카약을 빌릴 수 없으므로 ans 1 추가
    else:
        ans += 1

# 카약을 못 빌리는 팀의 최솟값 출력
print(ans)
