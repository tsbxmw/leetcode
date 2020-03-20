# 面试题 04.05. 合法二叉搜索树
# 实现一个函数，检查一棵二叉树是否为二叉搜索树。

# 示例 1:
# 输入:
#     2
#    / \
#   1   3
# 输出: true
# 示例 2:
# 输入:
#     5
#    / \
#   1   4
#      / \
#     3   6
# 输出: false
# 解释: 输入为: [5,1,4,null,null,3,6]。
#      根节点的值为 5 ，但是其右子节点值为 4 。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        self.temp = []

        def dfs(root):
            if root:
                dfs(root.left)
                self.temp.append(root.val)
                dfs(root.right)
        dfs(root)
        return self.temp == sorted(set(self.temp))
