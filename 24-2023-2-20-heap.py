 # heap 是一个二叉树， 二叉树节点是从上到下，从左到右依次添加节点的
# 如果节点数量闺女过了，那我们能知道二叉树长什么样子

# min heap: all partent node will be smaller than the child node

#heap pop 的工作原理（pop会删除最小的一个）， 如果想删除root节点，先把想删除的节点和tree的末端节点的的value 进行互换
#然后删除末端节点，然后整个tree 进行大小取值排序，在排序中，两个子节点需要进行比大小，跟小的进行互换， time complexity O（logn）

# 删除任意一个节点，需要用到hashmap。 hashmap的key 能区别每个节点
# 需要完成 lintcode heapify