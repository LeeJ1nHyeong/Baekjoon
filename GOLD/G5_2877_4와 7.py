k = int(input())

ans = ''

# k를 2로 나누면서 홀짝 여부에 따라 앞에 4 또는 7 추가
# k가 홀수일 경우 4로 끝나고, 짝수일 경우 7로 끝나는 성질을 이용
while k > 0:
    l = k % 2
    k //= 2

    if l:
        ans = "4" + ans
    else:
        k -= 1
        ans = "7" + ans

print(ans)