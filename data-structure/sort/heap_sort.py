def heapify(a, idx, n):
    l = idx*2
    r = idx*2 + 1
    s_idx = idx
    if l <= n and a[s_idx] > a[l]:
        s_idx = l
    if r <= n and a[s_idx] > a[r]:
        s_idx = r
    if s_idx != idx:
        a[idx], a[s_idx] = a[s_idx], a[idx]
        return heapify(a, s_idx, n)


def heap_sort(v):
    n = len(v)
    v = [0] + v

    # min heap
    for i in range(n, 0, -1):
        heapify(v, i, n)

    # min element extract & heap
    for i in range(n, 0, -1):
        print(v[1])
        v[i], v[1] = v[1], v[i]
        heapify(v, 1, i-1)


if __name__ == '__main__':
    a = [7,4,5,6,3,2,1]
    heap_sort(a)
