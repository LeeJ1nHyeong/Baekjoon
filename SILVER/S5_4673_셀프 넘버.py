num_list = [i for i in range(1, 10001)]

for i in range(1, 10001):
    i += (i // 10000) + (i // 1000) + ((i % 1000) // 100) + ((i % 100) // 10) + (i % 10)

    if i in num_list:
        num_list.remove(i)

for num in num_list:
    print(num)