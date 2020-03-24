# 面试题33. 二叉搜索树的后序遍历序列
# 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。


# 参考以下这颗二叉搜索树：

#      5
#     / \
#    2   6
#   / \
#  1   3
# 示例 1：

# 输入: [1,6,3,2,5]
# 输出: false
# 示例 2：

# 输入: [1,3,2,6,5]
# 输出: true
class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:

        # 使用递归可以解决
        # 由后向前遍历
        # 每个分部都是有顺序的，即 左子树，右子树，根节点
        # 而每个左子树都是这样构成的，只要从根节点向前寻找比根节点大的值，就是右子树，剩下的为左子树
        # 检查左子树中所有的值都小于 根节点
        # 递归求解 左子树，右子树
        def test(postorder):
            if not postorder or len(postorder) == 1:
                return True

            lp = len(postorder) - 1
            root = postorder[lp]
            right = []
            left = []
            i = lp - 1
            while i >= 0:
                if postorder[i] > root:
                    i -= 1
                else:
                    break
            left = postorder[:i+1]
            right = postorder[i+1:-1]
            for x in left:
                if x > root:
                    return False
            return test(right) and test(left)

        return test(postorder)
