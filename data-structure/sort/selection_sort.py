# 선택 정렬
# 주어진 데이터 내에서 가장 작은 데이터 찾기


def selection_sort(arr):
    for i in range(len(arr)):
        min_ = arr[i]
        loc = i
        for j in range(i+1, len(arr)):
            if min_ > arr[j]:
                min_ = arr[j]
                loc = j
        arr[i], arr[loc] = arr[loc], arr[i]
        print(arr)


arr = [3,2,3,1] #

selection_sort(arr)
print(arr)


# 착각한거
# def selection_sort(arr):
#     for i in range(len(arr)):
#         for j in range(i+1, len(arr)):
#             if arr[i] > arr[j]:
#                 arr[i], arr[j] = arr[j], arr[i]
# 위 코드는 주어진 데이터에서 최솟값을 찾는게 아니라
# 가장 가까운 최솟값을 찾는 것이므로 선택정렬이 아님