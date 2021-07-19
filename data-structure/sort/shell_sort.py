def gap_insertion_sort(arr, start, gap):
    for i in range(start+gap, len(arr), gap):
        val = arr[i]
        pos = i
        while pos > start and arr[pos-gap] > val:
            arr[pos] = arr[pos - gap]
            pos -= gap
        arr[pos] = val


def shell_sort(arr):
    gap = len(arr) // 2
    while gap > 0:
        for i in range(gap):
            gap_insertion_sort(arr, i, gap)
        gap //= 2
    return arr


if __name__ == '__main__':
    a = [2, 6, 1, 8, 4, 7, 3, 5]
    print(shell_sort(a))