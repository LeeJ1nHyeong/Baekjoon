import sys

word = list(str(sys.stdin.readline().rstrip()))
frula_word = list(str(sys.stdin.readline().rstrip()))
fl = len(frula_word)

stack = []

for w in word:
    stack.append(w)
    if stack[-fl:] == frula_word:
        for _ in range(fl):
            stack.pop()

if not stack:
    print('FRULA')
else:
    for s in stack:
        print(s, end='')