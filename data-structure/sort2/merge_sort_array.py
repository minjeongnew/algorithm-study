def merge_sort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    low = merge_sort(arr[:mid])
    high = merge_sort(arr[mid:])
    i1, i2 = 0, 0
    merged = []

    while i1 < len(low) and i2 < len(high):
        if low[i1] < high[i2]:
            merged.append(low[i1])
            i1 += 1
        else:
            merged.append(high[i2])
            i2 += 1
    merged += low[i1:]
    merged += high[i2:]
    return merged



if __name__ == '__main__':
    a = [27, 10, 8, 3, 12, 20, 25, 13, 15, 22]
    print(merge_sort(a))