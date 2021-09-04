import sys

class Node(object):
    def __init__(self, item, left, right):
        self.item = item
        self.left = left
        self.right = right


n = int(sys.stdin.readline())
trees = {}
for _ in range(n):
    item, left, right = map(str, sys.stdin.readline().split())
    trees[item] = Node(item=item, left=left, right=right)


def preorder(node):
    print(node.item, end='')
    if node.left != '.':
        preorder(trees[node.left])
    if node.right != '.':
        preorder(trees[node.right])


def inorder(node):
    if node.left != '.':
        inorder(trees[node.left])
    print(node.item, end='')
    if node.right != '.':
        inorder(trees[node.right])


def postorder(node):
    if node.left != '.':
        postorder(trees[node.left])
    if node.right != '.':
        postorder(trees[node.right])
    print(node.item, end='')

preorder(trees['A'])
print()
inorder(trees['A'])
print()
postorder(trees['A'])