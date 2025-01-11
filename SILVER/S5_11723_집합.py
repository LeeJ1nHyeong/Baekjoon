import sys
input = sys.stdin.readline

m = int(input())
s = set()

for _ in range(m):
    command = input().split()

    if command[0] == "add":
        x = int(command[1])
        s.add(x)

    elif command[0] == "remove":
        x = int(command[1])
        s.discard(x)

    elif command[0] == "check":
        x = int(command[1])
        print(1 if x in s else 0)

    elif command[0] == "toggle":
        x = int(command[1])

        if x in s:
            s.remove(x)
        else:
            s.add(x)

    elif command[0] == "all":
        s = set([i for i in range(1, 21)])

    elif command[0] == "empty":
        s = set()
