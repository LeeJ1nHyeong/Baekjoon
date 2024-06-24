def new_rank():
    # 랭킹판이 비어있다면 1 return
    if not n:
        return 1
    
    ranking = list(map(int, input().split()))
    # 랭킹판을 내림차순으로 정렬
    ranking.sort(reverse=True)

    # 랭킹판이 꽉 차있을 때 점수가 최저점 이하라면 -1 return
    if n == p:
        if score <= ranking[-1]:
            return -1
    
    # 랭킹판에 자리가 있을 때 점수가 최저점보다 낮다면 맨 뒤 등수로 return
    else:
        if score < ranking[-1]:
            return n + 1
        
    # 위 두 경우를 제외하고 랭킹판 탐색하여 등수 return
    for i in range(n):
        if score >= ranking[i]:
            return i + 1


n, score, p = map(int, input().split())

print(new_rank())
