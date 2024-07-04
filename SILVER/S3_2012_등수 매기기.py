n = int(input())
rank = [0]

# 예상 순위를 리스트에 추가
for _ in range(n):
    rank.append(int(input()))

# 예상 등수와 실제 등수의 차이 합을 최소로 만들려면 예상 등수를 오름차순 정렬하면 된다.
# 오름차순 정렬
rank.sort()

# 예상 등수와 실제 등수 차의 절대값 합을 출력
ans = 0
for i in range(1, n + 1):
    ans += abs(i - rank[i])
print(ans)
