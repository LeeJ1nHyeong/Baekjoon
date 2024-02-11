def pre_order(node):  # 전위 순회
    left, right = nodes[ord(node) - 65]
    # 루트, 왼쪽, 오른쪽 순서로 진행
    print(node, end="")
    if left != ".":
        pre_order(left)
    if right != ".":
        pre_order(right)


def in_order(node):  # 중위 순회
    left, right = nodes[ord(node) - 65]
    # 왼쪽, 루트, 오른쪽 순서로 진행
    if left != ".":
        in_order(left)
    print(node, end="")
    if right != ".":
        in_order(right)


def post_order(node):  # 후위 순회
    left, right = nodes[ord(node) - 65]
    # 왼쪽, 오른쪽, 루트 순으로 진행
    if left != ".":
        post_order(left)
    if right != ".":
        post_order(right)
    print(node, end="")


n = int(input())
nodes = [['', ''] for _ in range(n)]  # 트리

for _ in range(n):
    root, left, right = input().split()
    nodes[ord(root) - 65][0] = left
    nodes[ord(root) - 65][1] = right

pre_order("A")  # 전위 순회
print()
in_order("A")  # 중위 순회
print()
post_order("A")  # 후위 순회