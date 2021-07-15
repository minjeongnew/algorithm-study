def insertion_sort(arr):
    for i in range(2, len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                arr[j-1], arr[j] = arr[j], arr[j-1]

    return arr


if __name__ == '__main__':
    arr = [8,5,6,2,4]
    print(insertion_sort(arr))