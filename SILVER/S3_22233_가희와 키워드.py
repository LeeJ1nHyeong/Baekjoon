import sys
input = sys.stdin.readline

n, m = map(int, input().split())
memo = {}  # 메모장을 해시로 구현

# 메모장에 키워드 저장
for _ in range(n):
    memo[input().rstrip()] = 1

# 블로그에 작성한 글의 키워드 탐색
for _ in range(m):
    # 쉼표로 구분하여 리스트로 저장
    memo_list = list(input().rstrip().split(","))

    # 메모장에 단어가 있다면 삭제
    for ml in memo_list:
        if ml in memo.keys():
            del memo[ml]

    # 삭제 후 메모장에 남아있는 키워드 개수 출력
    print(len(memo))
