n = int(input())
start = {}
end = {}

for i in range(n):
    car = input()
    start[car] = i

for i in range(n):
    car = input()
    end[car] = i

cnt = 0
end_cars = list(end.keys())
for i in range(len(end_cars) - 1):
    now_car = start[end_cars[i]]
    for j in range(i + 1, len(end_cars)):
        next_car = start[end_cars[j]]
        if next_car < now_car:
            cnt += 1
            break

print(cnt)
