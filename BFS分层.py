# BFS分层

from collections import deque

def bfs(self, node):
    queue = deque([node])
    visited = set([node])
    while queue:
        # 主要是在这一步分层，下来都一样
        for _ in range(len(queue)):
            cur_node = queue.popleft()
            for neighbors in cur_node.get_neighbors():
                if neighbors in visited:
                    continue
            visited.add(neighbors)    
            #visited[neighbors] = visited[node]+1 用这个如果是hash
            queue.append(neighbors)

            
