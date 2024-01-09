n, k = map(int, input().split())
exp = list(map(int, input().split()))  # 경험치 리스트
exp.sort()  # 오름차순 정렬

ans = 0

'''
- 먼저 진행하는 퀘스트는 아케인스톤이 없는 상태이기 때문에 경험치 합산에서 제외
   => 경험치가 가장 낮은 퀘스트부터 진행
- 이후 최대 아케인스톤 활성화 개수까지 순차적으로 곱해주면서 경험치 합산 시키기
- 활성화 개수가 최대가 되면 경험치를 곱하여 합산시키기
'''
for i in range(1, n):
    if i <= k:
        ans += exp[i] * i
    else:
        ans += exp[i] * k

print(ans)