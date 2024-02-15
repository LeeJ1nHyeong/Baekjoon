import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def in_order(root):  # 중위 순회
    global cnt
    left, right = tree[root][0], tree[root][1]

    if left != -1:
        in_order(left)
        cnt += 1

    if right != -1:
        in_order(right)
        cnt += 1


def in_order_right(root):  # 오른쪽으로만 순회
    global right_cnt
    right = tree[root][1]

    if right != -1:
        in_order_right(right)
        right_cnt += 1


n = int(input())
tree = [[0, 0] for _ in range(n + 1)]

# 노드 간선 저장
for _ in range(n):
    node, left, right = map(int, input().split())
    tree[node][0] = left
    tree[node][1] = right

# 중위 순회할 때의 방문 횟수
cnt = 0
in_order(1)

# 오른쪽으로만 순회할 때의 방문 횟수
right_cnt = 0
in_order_right(1)

print(2 * cnt - right_cnt)  # 계산하여 출력