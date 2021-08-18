import sys
sys.setrecursionlimit(10**5)


class Tree:
    def __init__(self, datalist):
        self.idx, *self.root = datalist.pop()
        leftlist = []
        rightlist = []
        for data in datalist:
            if data[1] < self.root[0]:
                leftlist.append(data)
            else:
                rightlist.append(data)
        self.left = Tree(leftlist) if leftlist else None
        self.right = Tree(rightlist) if rightlist else None


def traversal(tree, pre, post):
    pre.append(tree.idx)
    if tree.left:
        traversal(tree.left, pre, post)
    if tree.right:
        traversal(tree.right, pre, post)
    post.append(tree.idx)


def solution(nodeinfo):
    nodeinfo2 = [(idx+1, x, y) for idx, (x, y) in enumerate(nodeinfo)]
    nodeinfo2.sort(key=lambda x:x[2])
    t = Tree(nodeinfo2)
    pre, post = [], []
    traversal(t, pre, post)
    return [pre, post]


if __name__ == "__main__":
    n = [[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]
    print(solution(n))