word = str(input())
length = len(word)
c_alpha = ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']

for i in range(len(word) - 1):
    for c in c_alpha:
        if word[i:i+2] == c:
            length -= 1

for i in range(len(word) - 2):
    if word[i:i+3] == 'dz=':
        length -= 1

print(length)