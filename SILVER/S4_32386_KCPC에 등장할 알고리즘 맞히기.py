n = int(input())
tag = {}

for _ in range(n):
    s, t, *a = input().split()

    for problem in a:
        if problem not in tag:
            tag[problem] = 1
        else:
            tag[problem] += 1

tag_list = list(tag.items())
tag_list.sort(key=lambda x: -x[1])

if len(tag_list) >= 2 and tag_list[0][1] == tag_list[1][1]:
    print(-1)
else:
    print(tag_list[0][0])
