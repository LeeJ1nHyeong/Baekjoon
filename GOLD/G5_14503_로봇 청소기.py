'''
1. 현재 칸(room[i][j])이 청소되지 않았다면 청소 진행(clean 함수 실행)
2. 청소 이후 주변 4칸을 탐색하여 청소 필요 구역 존재 여부 확인(search 함수 실행)
3. 청소 필요 구역 존재 여부에 따라 단계 진행
3-1. 청소 필요 구역이 존재한다면 청소 필요 구역 방향까지 반시계 회전(rotate 함수 실행) & 해당 구역 전진(go 함수 실행)
3-2. 청소 필요 구역이 없다면 후진(back 함수 실행)
    후진한 뒤의 좌표가 벽이라면 반복 종료, 아니면 1번으로 다시 돌아가서 반복 진행
'''

def clean():  # 현재 위치한 좌표 청소
    global room
    global cnt

    room[i][j] = 2  # 구역 청소 및 벽이 아니라는 의미로 2 표시
    cnt += 1

def search():  # 현재 위치에서 4방향 탐색
    clean_cnt = 0
    for k in range(4):
        ni, nj = i + di[k], j + dj[k]
        if 0 <= ni < n and 0 <= nj < m:
            if room[ni][nj] == 0:
                clean_cnt += 1

    return clean_cnt

def go():  # 전진
    global i, j

    i += di[d]
    j += dj[d]

def back():  # 후진
    global i, j

    i -= di[d]
    j -= dj[d]

def rotate():  # 반시계 회전
    global d

    d -= 1
    if d == -1:
        d = 3

    ni, nj = i + di[d], j + dj[d]
    # 방 범위 내에서 바라보는 방향에 청소가 필요하면 전진
    if 0 <= ni < n and 0 <= nj < m and room[ni][nj] == 0:
        go()
        return
    else:
        rotate()  # 청소가 필요 없으면 반시계회전

    return

n, m = map(int, input().split())
i, j, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]
cnt = 0  # 청소 횟수

# 북, 동, 남, 서 순서
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

while True:
    if not room[i][j]:  # 현재 위치에서 청소가 필요하다면 청소 진행
        clean()

    need_clean = search()  # 4방향 중 필요 청소구역 개수

    if need_clean:  # 필요 청소구역이 존재한다면 반시계방향 회전
        rotate()

    else:  # 없다면 후진
        back()
        if room[i][j] == 1:  # 후진한 뒤의 좌표가 벽이라면 while문 종료
            break

print(cnt)