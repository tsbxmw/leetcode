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


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        self.temp = []

        # 这里使用中序遍历为递增序列的原理

        def dfs(root):
            if root:
                dfs(root.left)
                self.temp.append(root.val)
                dfs(root.right)
        dfs(root)
        return self.temp == sorted(set(self.temp))

# 非递归方法
# 迭代


class Solution1:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True

        p = root
        stack = []
        rev = []
        while p or stack:
            while p:
                stack.append(p)
                p = p.left
            if stack:
                node = stack.pop()
                rev.append(node.val)
                p = node.right
        return rev == sorted(set(rev))


# 递归求解，不需要额外空间

class Solution2:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True

        def dfs(node, min_=-float('inf'), max_=float('inf')):
            if not node:
                return True
            if not (min_ < node.val < max_):
                return False
            return dfs(node.left, min_, node.val) and dfs(node.right, node.val, max_)

        return dfs(root)
