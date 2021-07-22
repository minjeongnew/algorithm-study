def partition(data, start, end):
    left = start
    right = end
    pivot = data[start]
    while left < right:
        while data[left] <= pivot and left < end:
            left += 1
        while data[right] >= pivot and right > start:
            right -= 1
        if left < right:
            data[left], data[right] = data[right], data[left]
    data[start], data[right] = data[right], data[start]
    return right


def quick_sort(data, start, end):
    if start < end:
        p = partition(data, start, end)
        quick_sort(data, start, p-1)
        quick_sort(data, p+1, end)


if __name__ == '__main__':
    a = [5,6,9,2,4,7,1,8]
    quick_sort(a, 0, len(a)-1)
    print(a)