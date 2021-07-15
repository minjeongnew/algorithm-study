def merge_sort(arr):

    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])
    print(low_arr, high_arr)
    merged = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged.append(low_arr[l])
            l += 1
        else:
            merged.append(high_arr[h])
            h += 1
    merged += low_arr[l:]
    merged += high_arr[h:]
    return merged


if __name__ == '__main__':
    a = [27, 10, 8, 3, 12, 20, 25, 13, 15, 22]
    print(merge_sort(a))