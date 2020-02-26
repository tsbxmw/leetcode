# 105. 从前序与中序遍历序列构造二叉树
# 根据一棵树的前序遍历与中序遍历构造二叉树。
#
# 注意:
# 你可以假设树中没有重复的元素。
#
# 例如，给出
#
# 前序遍历 preorder = [3,9,20,15,7]
# 中序遍历 inorder = [9,3,15,20,7]
# 返回如下的二叉树：
#
#     3
#    / \
#   9  20
#     /  \
#    15   7

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

## 题目比较简单：使用递归即可解决

class Solution:
    def buildTree(self, preorder, inorder) -> TreeNode:
        ln = len(preorder)
        if ln == 0:
            return None

        def test(preorder, inorder):
            if not inorder:
                return None
            root = TreeNode(preorder[0])
            pi = inorder.index(preorder[0])
            root.left = test(preorder[1:1+pi], inorder[:pi])
            root.right = test(preorder[pi+1:], inorder[pi+1:])
            return root

        return test(preorder, inorder)


if __name__ == "__main__":
    s = Solution()
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    print(s.buildTree(preorder, inorder))