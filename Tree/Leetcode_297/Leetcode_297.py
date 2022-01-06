##### Python 3 #####
##### Runtime 108ms, Memory 18.8MB #####

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
            