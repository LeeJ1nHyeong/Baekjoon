from collections import deque


# bfs
def bfs(s, e):
    # bfs 초기 세팅
    queue = deque([s])
    visited = [0] * 26
    visited[s] = 1

    # bfs 진행
    while queue:
        now = queue.popleft()

        for node in nodes[now]:
            # 목표 알파벳이라면 "T" return
            if node == e:
                return "T"

            # 방문한 알파벳이라면 continue
            if visited[node]:
                continue

            # 방문 표시 후 queue에 추가
            visited[node] = 1
            queue.append(node)

    return "F"  # while문이 종료됐다면 "F" return


n = int(input())
nodes = [[] for _ in range(26)]  # 알파벳 별로 다음 루트를 저장할 2차원 리스트

# 각 문장의 시작 알파벳과 끝 알파벳을 아스키 코드로 적절하게 변환하여 nodes에 저장
for _ in range(n):
    sentence = input()
    from_alpha, to_alpha = ord(sentence[0]) - 97, ord(sentence[-1]) - 97
    nodes[from_alpha].append(to_alpha)

# 각 결론이 참인지 거짓인지 bfs로 판별 진행
m = int(input())
for _ in range(m):
    sentence = input()
    from_alpha, to_alpha = ord(sentence[0]) - 97, ord(sentence[-1]) - 97
    print(bfs(from_alpha, to_alpha))
