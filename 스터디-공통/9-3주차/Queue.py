# 은행 업무
# 콜센터 고객 대깃 기나
# 프로세스 관리
# 너비우선탐색
# 캐시 구현

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, x):
        self.queue.append(x)

    def dequeue(self):
        if self.isEmpty():
            print("Queue is Empty")
            return
        else:
            return self.queue.pop(0)

    def isEmpty(self):
        return len(self.queue) == 0


if __name__ == "__main__":
    q = Queue()
    print(q.enqueue(1))
    print(q.enqueue(2))
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.enqueue(3))