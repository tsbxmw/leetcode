# 面试题37. 序列化二叉树
# 请实现两个函数，分别用来序列化和反序列化二叉树。

# 示例:

# 你可以将以下二叉树：

#     1
#    / \
#   2   3
#      / \
#     4   5

# 序列化为 "[1,2,3,null,null,4,5]"

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "[]"
        rev = []

        def bfs(node, floor):
            if floor == len(rev):  # 增加下面一行
                rev.append([])
            if node:
                rev[floor].append(node.val)  # 如果 node 存在，增加到行所在的列表
            else:
                rev[floor].append(None)  # 如果 node 为 None，增加到 行里，不往下搜索
                return
            bfs(node.left, floor+1)  # 搜索下一行
            bfs(node.right, floor+1)
        bfs(root, 0)
        temp = []
        for x in rev:
            if set(x) != {None}:
                for y in x:
                    temp.append(y)
        return str(temp).replace('None', 'null').replace(" ", "")

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 2:
            return None
        temp = [x for x in data[1:-1].split(',')]  # 这里转化一下 str ->> 列表
        lt = len(temp)
        pre = rev = dd = TreeNode(0)
        list_node = [rev]
        i = 0
        for node in list_node:  # 遍历列表
            if i >= lt:
                break
            if temp[i] == 'null':
                i += 1
                node = None
                continue
            node.val = temp[i]
            node.left = TreeNode(None)
            node.right = TreeNode(None)
            # 将 node.left 放在列表 后面，这样对应的位置与 temp 就相同了
            list_node.append(node.left)
            list_node.append(node.right)
            i += 1
        # 到这一步， 树已经构建好了，但是由于我们是从前往后构建，所以没有将 None 的节点表示出来，下面用 dfs 清除所有 val==None 的值

        def dfs(dd):
            if not dd:
                return
            dfs(dd.left)
            dfs(dd.right)
            if dd.left and dd.left.val is None:
                dd.left = None
            if dd.right and dd.right.val is None:
                dd.right = None
        dfs(dd)
        return pre

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
