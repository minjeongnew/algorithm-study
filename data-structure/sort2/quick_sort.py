def partition(data, left, right):
    pivot = data[left]
    l = left
    r = right
    while l < r:
        while data[l] <= pivot and l < right:
            l += 1
        while data[r] >= pivot and r > left:
            r -= 1
        if l < r:
            data[l], data[r] = data[r], data[l]
    data[left], data[r] = data[r], data[left]
    return r


def quick_sort(data, left, right):
    if left < right:
        p = partition(data, left, right)
        quick_sort(data, left, p-1)
        quick_sort(data, p+1, right)


if __name__ == '__main__':
    d = [5, 3, 8, 4, 9, 1, 6, 2, 7]
    quick_sort(d, 0, len(d)-1)
    print(d)