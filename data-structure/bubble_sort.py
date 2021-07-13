def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


if __name__ == '__main__':
    a = [7, 4, 5, 1, 3]
    bubble_sort(a)
    print(a)