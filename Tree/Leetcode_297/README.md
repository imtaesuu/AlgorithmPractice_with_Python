## - Leetcode 297 Serialize and Deserialize Binary Tree - [Link](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/)
● 입력  
> root = [1,2,3,null,null,4,5]

● 출력
> [1,2,3,null,null,4,5]

## - Code - [Link](https://github.com/imtaesuu/AlgorithmPractice_with_Python/blob/main/Tree/Leetcode_297/Leetcode_297.py)

```python
class Codec:

    def serialize(self, root):
        q = collections.deque([root])
        res = ['#']
        
        while q:
            node = q.popleft()
            if node:
                q.append(node.left)
                q.append(node.right)
                
                res.append(str(node.val))
            else:
                res.append('#')
        
        return ' '.join(res)            
        

    def deserialize(self, data):
        if data == '# #':
            return None
        
        nodes = data.split()
        root = TreeNode(nodes[1])
        q = collections.deque([root])
        
        idx = 2
        while q:
            node = q.popleft()
            
            if nodes[idx] != '#':
                node.left = TreeNode(nodes[idx])
                q.append(node.left)
            idx += 1
            
            if nodes[idx] != '#':
                node.right = TreeNode(nodes[idx])
                q.append(node.right)
            idx += 1
            
        return root

##### Python 3 #####
##### Runtime 108ms, Memory 18.8MB #####
```

## - **How To Solve**
- bfs와 러너 비스무리한 기법으로 풀이했던 문제
- 트리의 직렬화를 잘 이해하고 있다면, 역직렬화는 크게 어렵지 않다.
- 가장 중요한건 deque를 이용하여 bfs를 이용해야하는 것