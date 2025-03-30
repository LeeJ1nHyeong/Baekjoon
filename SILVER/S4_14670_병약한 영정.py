n = int(input())
medicine = dict()

for _ in range(n):
    me, mn = map(int, input().split())
    medicine[me] = mn

r = int(input())
for _ in range(r):
    l, *s = map(int, input().split())
    ans = []

    is_died = False
    for i in range(l):
        if s[i] not in medicine:
            is_died = True
            break

        ans.append(medicine[s[i]])

    if is_died:
        print("YOU DIED")
    else:
        print(*ans)
