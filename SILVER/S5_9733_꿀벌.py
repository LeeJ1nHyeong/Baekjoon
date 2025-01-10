bee = {
    "Re": 0,
    "Pt": 0,
    "Cc": 0,
    "Ea": 0,
    "Tb": 0,
    "Cm": 0,
    "Ex": 0
}

total = 0

while True:
    try:
        works = list(input().split())

        for work in works:
            total += 1
            if work not in bee:
                continue
            bee[work] += 1

    except EOFError:
        break

for b in bee:
    average = round(bee[b] / total, 2) if bee[b] else "0.00"

    print(f"{b} {bee[b]} {average}")

print(f"Total {total} 1.00")
