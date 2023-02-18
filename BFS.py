#BFS
class Solution:

    def levelorder(self,root):
        if not root:
            return []
            #把第一层节点放到队列中
        queue = collections.deque([root])

        #while 队列非空
        while queue:
            result = []
            result.append([node.val for node in queue])
            size = len(queue)
            for i in range (size):
                node = queue.popleft()
                #把上层节点拓展到下一次层
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result
