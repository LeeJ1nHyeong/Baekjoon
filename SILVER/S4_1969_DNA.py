n, m = map(int, input().split())
dna = []

for _ in range(n):
    dna.append(input())

ans = ""  # Hamming Distance 최솟값을 갖는 염기서열
ans_cnt = 0  # Hamming Distance 최솟값
item = ["A", "C", "G", "T"]

for j in range(m):
    # 각 dna의 염기서열을 탐색
    acgt = [0, 0, 0, 0]
    for i in range(n):
        if dna[i][j] == "A":
            acgt[0] += 1
        elif dna[i][j] == "C":
            acgt[1] += 1
        elif dna[i][j] == "G":
            acgt[2] += 1
        elif dna[i][j] == "T":
            acgt[3] += 1

    # 가장 많은 염기서열을 ans에 추가
    # 개수가 같을 경우, 알파벳 순서로 결정
    ans += item[acgt.index(max(acgt))]
    # 
    ans_cnt += n - max(acgt)

# DNA와 Hamming Distance 최솟값 출력
print(ans)
print(ans_cnt)
