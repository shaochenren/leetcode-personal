#平衡二叉树定义： 任意节点左右子树高度之差不超过1
def isbalanced(self,root):
    is_balanced, _ = divideconquer(root)
    return is_balanced
def divideconquer(self,root):
    if not root:
        return True, 0
    is_left_balanced,left_height = self.divideconquer(root,left)
    is_right_balanced, right_height = self.divideconquer(root.right)
    root_height = max(left_height,right_height) +1

    if not is_left_balanced or not is_right_balanced:
        return False,root_height
    if abs(left_height -right_height) >1:
        return False,root_height
    return True, root_height

