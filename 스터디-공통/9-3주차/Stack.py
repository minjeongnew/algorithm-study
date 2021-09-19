# top으로 정한 곳을 통해서만 접근 가능
# push / pop
# LIFO
# 역순 문자열 만들기
# 웹 페이지 방문기록(뒤로가기)
# 후위 교기법 계산

class Stack:
    def __init__(self):
        self.stack = []

    def __len__(self):
        return len(self.stack)

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            print("Stack Underflow")
            # exit(
            return

    def clear(self):
        self.stack = []

    def isEmpty(self):
        return len(self.stack) == 0

    def isContain(self, x):
        return x in self.stack