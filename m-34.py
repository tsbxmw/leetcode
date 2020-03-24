# 面试题34. 二叉树中和为某一值的路径
# 输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。从树的根节点开始往下一直到叶节点所经过的节点形成一条路径。


# 示例:
# 给定如下二叉树，以及目标和 sum = 22，

#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1
# 返回:

# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]


# 提示：

# 节点总数 <= 10000

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        # 这个还是 dfs，深度搜索即可，加入值去计算
        self.rev = []
        if not root:
            return self.rev

        def dfs(node, value, temp):
            if not node:
                return
            value = value - node.val
            temp.append(node.val)
            if node and not node.left and not node.right:  # 当节点为叶子节点时，才会判断是否加入到结果中去
                if value == 0:
                    self.rev.append(temp)
            dfs(node.left, value, temp[:])
            dfs(node.right, value, temp[:])

        dfs(root, sum, [])
        return self.rev
