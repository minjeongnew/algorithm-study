def partition(a, left, right):
    mid = (left+right) // 2
    a[left], a[mid] = a[mid], a[left]
    pivot = a[left]
    print(pivot)
    i = left
    j = right
    # print(a)
    while i < j:
        while pivot < a[j]:
            j -= 1
        while pivot >= a[i] and i < j:
            i += 1
        a[i], a[j] = a[j], a[i]
        # print(a)
    a[left] = a[i]
    a[i] = pivot
    # print(a)
    return i


def quicksort(a, left, right):
    if left >= right:
        return
    pivot = partition(a, left, right)
    quicksort(a, left, pivot-1)
    quicksort(a, pivot+1, right)
a = [9, 5, 3, 7, 4, 2, 1, 8]
quicksort(a, 0, len(a)-1)
print(a)