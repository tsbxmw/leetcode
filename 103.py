# 给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

# 例如：
# 给定二叉树 [3,9,20,null,null,15,7],

#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回锯齿形层次遍历如下：

# [
#   [3],
#   [20,9],
#   [15,7]
# ]

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


## 广度优先遍历，分层再重新倒序即可。
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        temp = []
        if not root:
            return None
        def test(node, level):
            if not node:
                return
            if len(temp) <= level:
                temp.append([])
            temp[level].append(node.val)
            test(node.left, level+1)
            test(node.right, level+1)
        test(root, 0)
        for i in range(len(temp)):
            if i%2 == 1:
                temp[i] = temp[i][::-1]

        return temp
