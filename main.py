import sys, datetime , math, itertools, random
from collections import Counter, defaultdict, deque
import heapq
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root
        return None
            