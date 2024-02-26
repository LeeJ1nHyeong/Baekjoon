n = int(input())
books = {}  # 판매한 책을 담을 딕셔너리

# 딕셔너리 내에 해당 책이 있지 않다면 key로 새로 생성
for _ in range(n):
    book = input()
    # 딕셔너리 내에 해당 책이 있지 않다면 key로 새로 생성
    if book not in books:
        books[book] = 1
    # 있다면 1 추가
    else:
        books[book] += 1

# 책의 판매 횟수 내림차순, 같을 시 이름 오름차순으로 정렬하여 tuple 형식으로 저장
books = sorted(books.items(), key=lambda x: (-x[1], x[0]))

print(books[0][0])  # 가장 많이 팔린 책의 이름 출력