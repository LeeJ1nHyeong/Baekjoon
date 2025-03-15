# 병합 정렬 구현

def merge_sort(lst, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(lst, p, q)
        merge_sort(lst, q + 1, r)
        merge(lst, p, q, r)


def merge(lst, p, q, r):
    global cnt, result

    left, right = p, q + 1
    merge_list = []

    while left <= q and right <= r:
        if lst[left] <= lst[right]:
            merge_list.append(lst[left])
            left += 1
        else:
            merge_list.append(lst[right])
            right += 1

    while left <= q:
        merge_list.append(lst[left])
        left += 1

    while right <= r:
        merge_list.append(lst[right])
        right += 1

    idx = p
    merge_idx = 0

    while idx <= r:
        lst[idx] = merge_list[merge_idx]
        cnt += 1

        if cnt == k:
            result = lst[idx]
            break

        idx += 1
        merge_idx += 1


n, k = map(int, input().split())
numbers = list(map(int, input().split()))
cnt = 0
result = -1
merge_sort(numbers, 0, n - 1)
print(result)
