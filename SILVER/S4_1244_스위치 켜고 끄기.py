def change(i):
    if switch[i] == 0:
        switch[i] = 1
    else:
        switch[i] = 0

def man(x):
    switch_num = x - 1
    for i in range(switch_num, n, x):
        change(i)

def woman(x):
    switch_num = x - 1
    change(switch_num)
    i = 1
    while True:
        if (switch_num - i) < 0 or (switch_num + i) >= n:
            break
        if switch[switch_num - i] != switch[switch_num + i]:
            break
        change(switch_num - i)
        change(switch_num + i)

        i += 1

n = int(input())
switch = list(map(int, input().split()))
m = int(input())

for _ in range(m):
    gender, switch_start = map(int, input().split())
    if gender == 1:
        man(switch_start)
    else:
        woman(switch_start)

for i in range(0, n, 20):
    print(*switch[i: i + 20])