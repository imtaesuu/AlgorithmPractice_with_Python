import sys, datetime , math, itertools
from collections import Counter, defaultdict
import heapq
    
input = sys.stdin.readline

        
N = int(input())
tree = {}
for _ in range(N):
    root, left, right = input().split()
    tree[root] = [left, right]

def preorder_traversal(root):
    if root != '.':
        print(root, end = '')
        preorder_traversal(tree[root][0])
        preorder_traversal(tree[root][1])

def inorder_traversal(root):
    if root != '.':
        inorder_traversal(tree[root][0])
        print(root, end = '')
        inorder_traversal(tree[root][1])

def postorder_traversal(root):
    if root != '.':
        postorder_traversal(tree[root][0])
        postorder_traversal(tree[root][1])
        print(root, end = '')

print(preorder_traversal('A'))
print()
print(inorder_traversal('A'))
print()
print(postorder_traversal('A'))