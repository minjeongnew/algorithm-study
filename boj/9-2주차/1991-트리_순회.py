import sys

class Node:
    def __init__(self, item, left, right):
        self.item = item
        self.left = left
        self.right = right

n = int(sys.stdin.readline())
trees = {}
for _ in range(n):
    a, b, c = map(str, sys.stdin.readline().split())
    trees[a] = Node(a, b, c)


def preorder(x):
    print(trees[x].item, end = '')
    if trees[x].left != '.':
        preorder(trees[x].left)
    if trees[x].right != '.':
        preorder(trees[x].right)
def inorder(x):
    if trees[x].left != '.':
        inorder(trees[x].left)
    print(trees[x].item, end = '')
    if trees[x].right != '.':
        inorder(trees[x].right)
def postorder(x):
    if trees[x].left != '.':
        postorder(trees[x].left)
    if trees[x].right != '.':
        postorder(trees[x].right)
    print(trees[x].item, end = '')

preorder('A')
print()
inorder('A')
print()
postorder('A')