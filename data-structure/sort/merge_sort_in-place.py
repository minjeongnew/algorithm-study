def merge_sort(arr):
    n = len(arr)
    if n < 2:
        return

    mid = n // 2
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
    # 아직 남아있는 자료들을 결과에 추가
    while i1 < len(low):
        arr[ia] = low[i1]
        i1 += 1
        ia += 1
    while i2 < len(high):
        arr[ia] = high[i2]
        i2 += 1
        ia += 1


if __name__ == '__main__':
    a = [27, 10, 8, 3, 12, 20, 25, 13, 15, 22]
    merge_sort(a)
    print(a)

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
#
# class Sort:
#     def mergeTwoLists(self, l1:ListNode, l2:ListNode) -> ListNode:
#         if l1 and l2:
#             if l1.val > l2.val:
#                 l1, l2 = l2, l1
#             # 원래 연결된 값이랑 병합하면서 새로 만난 더 큰 값이랑 비교
#             l1.next = self.mergeTwoLists(l1.next, l2)
#         return l1 or l2 # 더 작은 값 반환
#
#     def sortList(self, head:ListNode) -> ListNode:
#         if not (head and head.next):
#             return head
#         # runner 기법으로 분할
#         half, slow, fast = None, head, head
#         while fast and fast.next:
#             half, slow, fast = slow, slow.next, fast.next.next
#         half.next = None # 분할
#
#         # 분할 재귀
#         l1 = self.sortList(head)
#         l2 = self.sortList(slow)
#
#         return self.mergeTwoLists(l1, l2)
