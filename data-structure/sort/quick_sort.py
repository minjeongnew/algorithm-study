def partition(data, left, right):
    pivot = data[left]
    i = left
    j = right
    while i < j:
        print(data)
        while data[i] <= pivot and i < right:
            i += 1
        while data[j] >= pivot and j > left:
            j -= 1
        if i < j:
            data[i], data[j] = data[j], data[i]
    data[left], data[j] = data[j], data[left]
    return j


def quick_sort(data, left, right):
    if left < right:
        q = partition(data, left, right)
        quick_sort(data, left, q-1)
        quick_sort(data, q+1, right)


if __name__ == '__main__':
    a = [5, 3, 8, 4, 9, 1, 6, 2, 7]
    quick_sort(a, 0, len(a)-1)
    print(a)
    b = [5, 4, 9, 0, 3, 1, 6, 2, 7, 8]
    quick_sort(b, 0, len(b)-1)
    print(b)