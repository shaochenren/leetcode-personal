# 69
class solution:
    def levelorder(self,root):
        if not root:
            return []
        
        q = collections.deque([root])
        result = []
        while q:
            result.append(node.val for node in q)
            size = len(q)
            for i in size:
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            return result