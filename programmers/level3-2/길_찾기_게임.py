class Tree:
    def __init__(self, nodeinfo):
        self.idx, *self.root = nodeinfo.pop()
        leftlist = []
        rightlist = []
        for node in nodeinfo:
            weight, x, y = node
            if x < self.root[0]:
                leftlist.append(node)
            else:
                rightlist.append(node)
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
    nodeinfo2 = []
    for idx, (x, y) in enumerate(nodeinfo):
        nodeinfo2.append([idx+1, x, y])
    nodeinfo2.sort(key=lambda x:x[2])
    t = Tree(nodeinfo2)
    pre, post = [], []
    traversal(t, pre, post)
    return [pre, post]


if __name__ == "__main__":
    n = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
    print(solution(n))