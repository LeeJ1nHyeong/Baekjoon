n = int(input())
topping = list(input().split())
cheese = set()

for t in topping:
    if t[-6:] == "Cheese":
        cheese.add(t)

print("yummy" if len(cheese) >= 4 else "sad")
