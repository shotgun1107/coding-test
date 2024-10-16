tree = {}

for _ in range(int(input())):
    root, left, right = input().split()
    tree[root] = [left, right]

def preorder(node):
    if node != '.':
        print(node, end='')
        preorder(tree[node][0])
        preorder(tree[node][1])

def inorder(node):
    if node != '.':
        inorder(tree[node][0])
        print(node, end='')
        inorder(tree[node][1])

def postorder(node):
    if node != '.':
        postorder(tree[node][0])
        postorder(tree[node][1])
        print(node, end='')

root = list(tree.keys())[0]

preorder(root)
print()
inorder(root)
print()
postorder(root)