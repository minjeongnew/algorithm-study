# idx / in-place

def merge_sort(arr):
    if len(arr) < 2:
        return

    mid = len(arr) // 2
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
    while i1 < len(low):
        arr[ia] = low[i1]
        i1 += 1
        ia += 1
    while i2 < len(high):
        arr[ia] = high[i2]
        i2 += 1
        ia += 1


if __name__ == "__main__":
    a = [27, 10, 8, 3, 12, 20, 25, 40, 13, 15, 22]
    merge_sort(a)
    print(a)