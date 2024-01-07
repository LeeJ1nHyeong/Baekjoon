# 분할정복을 이용한 풀이

def star(n):
    if n == 3:
        return ['***', '* *', '***']
    division = star(n // 3)
    star_list = []  # 별 문양을 담을 리스트

    for d in division:
        star_list.append(d * 3)
    for d in division:
        star_list.append(d + ' ' * (n // 3) + d)
    for d in division:
        star_list.append(d * 3)

    return star_list

n = int(input())

for s in star(n):
    print(s)