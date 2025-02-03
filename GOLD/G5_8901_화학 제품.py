t = int(input())

for _ in range(t):
    a, b, c = map(int, input().split())
    ab, bc, ca = map(int, input().split())

    max_price = 0

    for ab_cnt in range(min(a, b) + 1):
        bc_cnt = min(b - ab_cnt, c)
        ca_cnt = min(c - bc_cnt, a - ab_cnt)
        price = ab * ab_cnt + bc * bc_cnt + ca * ca_cnt
        max_price = max(price, max_price)

        ca_cnt = min(c, a - ab_cnt)
        bc_cnt = min(b - ab_cnt, c - ca_cnt)
        price = ab * ab_cnt + bc * bc_cnt + ca * ca_cnt
        max_price = max(price, max_price)

    print(max_price)
