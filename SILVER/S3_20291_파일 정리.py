n = int(input())
extensions = {}  # 파일의 확장자 별 개수를 저장할 해쉬

for _ in range(n):
    # 이름과 확장자를 구분
    name, extension = input().split(".")

    # 해쉬 내에 확장자가 없으면 key로 추가
    if extension not in extensions:
        extensions[extension] = 1
    # 있다면 해당 key의 value를 1 추가
    else:
        extensions[extension] += 1

# 이름 오름차순으로 정렬
extensions = sorted(extensions.items())

# 정렬 후 확장자명과 파일 개수 출력
for e in extensions:
    print(*e)
    