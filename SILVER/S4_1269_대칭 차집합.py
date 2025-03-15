a, b = map(int, input().split())
set_a = set(map(int, input().split()))
set_b = set(map(int, input().split()))
a_minus_b = set_a - set_b
b_minus_a = set_b - set_a

print(len(a_minus_b) + len(b_minus_a))
