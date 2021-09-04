import sys


class Node(object):
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right


def preorder(node):
    print(node.data, end='')
    if node.left:
        preorder(trees[node.left])
    if node.right:
        preorder(trees[node.right])


def inorder(node):
    if node.left:
        inorder(trees[node.left])
    print(node.data, end='')
    if node.right:
        inorder(trees[node.right])


def postorder(node):
    if node.left:
        postorder(trees[node.left])
    if node.right:
        postorder(trees[node.right])
    print(node.data, end='')


n = int(sys.stdin.readline())
trees = {}
for _ in range(n):
    data, left, right = map(str, sys.stdin.readline().split())
    if left == '.':
        left = None
    if right == '.':
        right = None
    trees[data] = Node(data=data, left=left, right=right)

preorder(trees['A'])
print()
inorder(trees['A'])
print()
postorder(trees['A'])
