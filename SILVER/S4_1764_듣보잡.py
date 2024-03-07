n, m = map(int, input().split())
member_a = set()  # 듣도 못한 사람
member_b = set()  # 보도 못한 사람
ab = []  # 듣도 보도 못한 사람

# 듣도 못한 사람을 집합에 추가
for _ in range(n):
    member = input()
    member_a.add(member)

# 보도 못한 사람을 집합에 추가
for _ in range(m):
    member = input()
    member_b.add(member)

ab = sorted(list(member_a & member_b))  # 두 집합의 교집합을 리스트에 담기

# 출력
print(len(ab))
for a in ab:
    print(a)