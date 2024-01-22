from collections import deque

def spring_summer():  # 봄, 여름
    global trees

    for r in range(n):
        for c in range(n):
            if trees[r][c]:
                alive_tree = deque()
                death_tree = 0  # 죽은 나무의 양분
                for tree in trees[r][c]:
                    age = tree

                    # 나무의 나이 만큼 양분을 사용한 뒤 1살 증가시킨 값을 alive_tree에 추가
                    if age <= ground[r][c]:
                        ground[r][c] -= age
                        alive_tree.append(age + 1)

                    # 양분이 부족하면 나이를 2로 나눈 몫을 death_tree에 더함
                    else:
                        death_tree += age // 2

                ground[r][c] += death_tree  # 죽은 나무들의 양분을 땅에 저장
                trees[r][c] = alive_tree  # 해당 좌표에서 생존한 나무를 새로 저장

def fall():  # 가을
    global trees

    new_trees = []  # 
    for r in range(n):
        for c in range(n):
            if trees[r][c]:
                for tree in trees[r][c]:
                    age = tree
                    if age % 5 == 0:  # 나무의 나이가 5의 배수일 때 주변 8방향 중 심을 수 있는 곳에 나이가 1인 나무가 새로 생성
                        for dr, dc in (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1):
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < n and 0 <= nc < n:
                                new_trees.append((nr, nc))

    # 나이가 1인 나무를 해당 좌표의 맨 왼쪽에 추가
    for tree in new_trees:
        r, c = tree
        trees[r][c].appendleft(1)

def winter():  # 겨울
    for r in range(n):
        for c in range(n):
            ground[r][c] += nutrients[r][c]  # 땅에 영양분 공급

n, m, k = map(int, input().split()) 

nutrients = [list(map(int, input().split())) for _ in range(n)]  # 겨울에 땅에 공급할 영양분
ground = [[5] * n for _ in range(n)]  # 처음 땅의 양분 상태
trees = [[deque() for _ in range(n)] for _ in range(n)]  # 나무의 나이를 담을 3차원 배열(실행 시간 제한때문에 deque 활용)

# 처음에 심어진 나무의 나이를 해당 좌표에 저장
for _ in range(m):
    r, c, age = map(int, input().split())
    trees[r - 1][c - 1].append(age)

for _ in range(k):
    spring_summer()  # 봄, 여름
    fall()  # 가을
    winter()  # 겨울

ans = 0  # k년 후 남아있는 나무의 그루 수

for i in range(n):
    for j in range(n):
        ans += len(trees[i][j])

print(ans)