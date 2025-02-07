s = list(input())
zero = s.count("0")
one = s.count("1")

one_cnt = 0
for i in range(len(s)):
    if one_cnt == one // 2:
        break

    if s[i] == "1":
        s.remove(s[i])
        one_cnt += 1

s = s[::-1]
zero_cnt = 0
for i in range(len(s)):
    if zero_cnt == zero // 2:
        break

    if s[i] == "0":
        s.remove(s[i])
        zero_cnt += 1

s = s[::-1]
print("".join(s))
