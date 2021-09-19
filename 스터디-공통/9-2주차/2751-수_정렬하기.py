import sys
n = int(sys.stdin.readline())
x = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

def merge_sort(arr):
    n = len(arr)
    if n < 2:
        return

    mid = n // 2
    low = arr[:mid]
    high = arr[mid:]
    merge_sort(low)
    merge_sort(high)

    i1, i2, ia = 0, 0, 0

    while i1 < len(low) and i2 < len(high):
        if low[i1] < high[i2]:
            arr[ia] = low[i1]
            i1 += 1
            ia += 1
        else:
            arr[ia] = high[i2]
            i2 += 1
            ia += 1
    # 아직 남아있는 자료들을 결과에 추가
    while i1 < len(low):
        arr[ia] = low[i1]
        i1 += 1
        ia += 1
    while i2 < len(high):
        arr[ia] = high[i2]
        i2 += 1
        ia += 1

merge_sort(x)
for i in x:
    print(i)
# 퀵소트
# import sys
#
# n = int(sys.stdin.readline())
#
#
# def partition(a, left, right):
#     mid = (left+right) // 2
#     a[left], a[mid] = a[mid], a[left]
#     pivot = a[left]
#     i = left
#     j = right
#     # print(a)
#     while i < j:
#         while pivot < a[j] and i < j: # 순서 바뀌면 안됨, j
#             j -= 1
#         while pivot >= a[i] and i < j:
#             i += 1
#         a[i], a[j] = a[j], a[i]
#         # print(a)
#     a[left] = a[i]
#     a[i] = pivot
#     # print(a)
#     return i
#
#
# def quicksort(a, left, right):
#     if left >= right:
#         return
#     pivot = partition(a, left, right)
#     # print(pivot)
#     quicksort(a, left, pivot-1)
#     # print(left, pivot, right)
#     quicksort(a, pivot+1, right)
#
# x = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
# quicksort(x, 0, n-1)
# print(x)