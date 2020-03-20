# 面试题 04.06. 后继者
# 设计一个算法，找出二叉搜索树中指定节点的“下一个”节点（也即中序后继）。

# 如果指定节点没有对应的“下一个”节点，则返回null。

# 示例 1:

# 输入: root = [2,1,3], p = 1

#   2
#  / \
# 1   3

# 输出: 2
# 示例 2:

# 输入: root = [5,3,6,2,4,null,null,1], p = 6

#       5
#      / \
#     3   6
#    / \
#   2   4
#  /
# 1

# 输出: null

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 这个也是深度搜索


class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        self.flag = False  # 使用 flag 标记

        def dfs(root):
            if root:
                left = dfs(root.left)
                if left:
                    return left
                if self.flag:
                    return root
                if root == p:
                    self.flag = True
                right = dfs(root.right)
                if right:
                    return right
        return dfs(root)
