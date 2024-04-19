import sys
input = sys.stdin.readline


t = int(input())

for _ in range(t):
    n = int(input())
    candidates = []  # 지원자의 서류 순위, 면접 순위를 담을 리스트

    # 서류 순위, 면접 순위를 튜플 형태로 리스트에 저장 후 서류 순위를 기준으로 오름차순 정렬
    for _ in range(n):
        d, i = map(int, input().split())
        candidates.append((d, i))
    candidates.sort()

    d_rank, i_rank = candidates[0]  # 서류 순위 1위의 서류 순위, 면접 순위
    ans = 1  # 최대 인원 수

    # 서류 순위는 항상 낮은 순위이므로 면접 순위만 비교해서 더 높은 순위일 경우 ans 1 추가 후 변수 최신화
    for d, i in candidates[1:]:
        if i < i_rank:
            d_rank, i_rank = d, i
            ans += 1

    print(ans)  # 최대 인원 수 출력
