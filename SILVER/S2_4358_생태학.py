trees = {}
total = 0

while True:
    try:
        tree = input()
        total += 1

        if tree in trees:
            trees[tree] += 1
        else:
            trees[tree] = 1

    except EOFError:
        break

trees = sorted(trees.items())

for tree, cnt in trees:
    print(f"{tree} {cnt / total * 100:.4f}")
