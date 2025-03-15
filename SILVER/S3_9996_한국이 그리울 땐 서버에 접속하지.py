n = int(input())
pattern = input().split("*")

for _ in range(n):
    file = input()

    if len(file) < len(pattern[0] + pattern[1]):
        print("NE")
        continue

    if file.startswith(pattern[0]) and file.endswith(pattern[1]):
        print("DA")
    else:
        print("NE")
