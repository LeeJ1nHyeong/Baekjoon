n = int(input())
names = input().split()
name_dict = {}

for name in names:
    name_dict[name] = 0

for _ in range(n):
    lst = input().split()
    for l in lst:
        name_dict[l] += 1

name_list = list(name_dict.items())
name_list.sort(key=lambda x: (-x[1], x[0]))

for nl in name_list:
    print(*nl)

