# 94. 二叉树的中序遍历
# 给定一个二叉树，返回它的中序 遍历。
#
# 示例:
#
# 输入: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
#
# 输出: [1,3,2]
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# 递归 1 ： 简单

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self.rev = []

        def dfs(root):
            if not root:
                return None
            dfs(root.left)
            self.rev.append(root.val)
            dfs(root.right)

        dfs(root)
        return self.rev


# 迭代 2： 修改代码
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        temp = []
        rev = []

        while temp or root:
            while root:
                temp.append(root)
                root = root.left
            root = temp.pop()
            rev.append(root.val)
            root = root.right
        return rev

