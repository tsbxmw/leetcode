# 1110. 删点成林
# 给出二叉树的根节点 root，树上每个节点都有一个不同的值。

# 如果节点值在 to_delete 中出现，我们就把该节点从树上删去，最后得到一个森林（一些不相交的树构成的集合）。

# 返回森林中的每棵树。你可以按任意顺序组织答案。


# 示例：


# 输入：root = [1,2,3,4,5,6,7], to_delete = [3,5]
# 输出：[[1,2,null,4],[6],[7]]


# 提示：

# 树中的节点数最大为 1000。
# 每个节点都有一个介于 1 到 1000 之间的值，且各不相同。
# to_delete.length <= 1000
# to_delete 包含一些从 1 到 1000、各不相同的值。

# dfs

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:

        if not root:
            return []

        self.to_delete = to_delete
        self.temp = []

        def dfs(node):
            if node and not node.left and not node.right:
                return
            if node.left:  # 找到最终的 left node
                dfs(node.left)
            if node.right:  # 找到最终的 right node
                dfs(node.right)
            if node.left and node.left.val in self.to_delete:  # 如果当前节点 的 左子树 是需要删除的，就删除它，因为 我们找到的是最下面的树
                node.left = None
            if node.right and node.right.val in self.to_delete:  # 如果当前节点 的 右子树 是需要删除的，就删除它
                node.right = None
            # 这里如果当前节点是需要删除的，就把存在的子树存到结果里
            # 注意，不能在这里删除 node，因为我们在上层遍历时，还是会进行删除操作的，没有必要重复
            if node.val in self.to_delete:
                if node.left:
                    self.temp.append(node.left)
                if node.right:
                    self.temp.append(node.right)
                return
        dfs(root)
        # 这里注意，如果最终 root 节点不需要删除的话，我们需要将它放置到 结果中
        if root.val not in self.to_delete:
            self.temp.append(root)
        return self.temp
