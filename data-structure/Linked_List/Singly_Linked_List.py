class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

# 단일 연결 리스트
class SinglyLinkedList(object):
    def __init__(self):
        self.head = None
        self.count = 0

    # add new node at the end of the linked list
    def append(self, node):
        if self.head == None:
            self.head = node
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    # return first index of data int the linked list
    # 데이터와 일치하는 첫번째 노드의 인덱스를 반환
    # If the given data is not existed, then return -1
    def getdataIndex(self, data):
        cur = self.head
        idx = 0
        while cur:
            if cur.data == data:
                return idx
            cur = cur.next
            idx += 1
        return -1

    # add new node at the given index
    # 주어진 인덱스에 새로운 노드 삽입
    def insertNodeAtIndex(self, idx, node):
        # 3가지 경우의 수
        # (1) 연결리스트의 맨 처음에
        # (2) 주어진 인덱스에
        # (3) 연결리스트 끝에
        cur_node = self.head
        prev_node = None
        cur_idx = 0

        # (1) add 0 index
        if idx == 0:
            if self.head:
                next_node = self.head
                self.head = node
                self.head.next = next_node
            else:
                self.head = node
        else:
            # (2) add at give index
            # (3) at the end of the linked list
            while cur_idx < idx:
                if cur_node:
                    prev_node = cur_node
                    cur_node = cur_node.next
                else:
                    break
                cur_idx += 1
            if cur_idx == idx:
                node.next = cur_node
                prev_node.next = node
            else:
                return -1

    # add new node before the given data
    def insertNodeAtData(self, data, node):
        idx = self.getdataIndex(data)
        if idx >= 0:
            self.insertNodeAtIndex(idx, node)
        else:
            return -1

    # delete data at given idx
    def deleteAtIndex(self, idx):
        cur_idx = 0
        cur_node = self.head
        prev_node = None
        next_node = self.head.next
        if idx == 0:
            self.head = next_node
        else:
            while cur_idx < idx:
                if cur_node.next:
                    prev_node = cur_node
                    cur_node = cur_node.next
                    next_node = next_node.next
                else:
                    break
                cur_idx += 1
            if cur_idx == idx:
                prev_node.next = next_node
            else:
                return -1

    # empty linked list
    def clear(self):
        self.head = None

    # print
    def print(self):
        cur_node = self.head
        s = ""
        while cur_node:
            s += str(cur_node.data)
            if cur_node.next:
                s += "->"
            cur_node = cur_node.next
        print(s)


if __name__ == "__main__":
    sl = SinglyLinkedList()
    sl.append(Node(1))
    sl.append(Node(2))
    sl.append(Node(3))
    sl.append(Node(4))
    sl.append(Node(3))
    sl.append(Node(5))
    sl.insertNodeAtIndex(2, Node(4))
    sl.print()
    sl.deleteAtIndex(0)
    sl.print()