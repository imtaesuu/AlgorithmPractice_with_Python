class Tree:
    def __init__(self):
        self.root = None
    
    def __str__(self):
        return self.root
    
    def link_node(self, node, left_node, right_node):
        if self.root == None:
            self.root = node
        node.left = left_node
        node.right = right_node

class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __str__ (self):
        return '{} -> ( {} {} )'.format(self.val, self.left, self.right)