# 138. 复制带随机指针的链表
# 给定一个链表，每个节点包含一个额外增加的随机指针，该指针可以指向链表中的任何节点或空节点。

# 要求返回这个链表的 深拷贝。

# 我们用一个由 n 个节点组成的链表来表示输入/输出中的链表。每个节点用一个 [val, random_index] 表示：

# val：一个表示 Node.val 的整数。
# random_index：随机指针指向的节点索引（范围从 0 到 n-1）；如果不指向任何节点，则为  null 。


# 示例 1：


# 输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# 输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]
# 示例 2：


# 输入：head = [[1,1],[2,1]]
# 输出：[[1,1],[2,1]]
# 示例 3：


# 输入：head = [[3,null],[3,0],[3,null]]
# 输出：[[3,null],[3,0],[3,null]]
# 示例 4：

# 输入：head = []
# 输出：[]
# 解释：给定的链表为空（空指针），因此返回 null。


# 提示：

# -10000 <= Node.val <= 10000
# Node.random 为空（null）或指向链表中的节点。
# 节点数目不超过 1000 。


# https://leetcode-cn.com/problems/copy-list-with-random-pointer/

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        if not head.next:
            if head.random is not None:
                n = Node(head.val, None)
                n.random = n
                return n
            else:
                return Node(head.val, None)

        head_list = []  # 存储 head 节点
        random_list = []  # 存储对应 head 节点对应的 random 节点
        copy_list = []  # 存储 copy 节点

        rev = copy_node_1 = copy_node = Node(0, None)

        while head:
            head_list.append(head)
            random_list.append(head.random)
            copy_node.val = head.val
            if head.next:  # 这里注意，当 head.next 为 None 时，copy 的 next 也是 None
                copy_node.next = Node(0, None)
                copy_node = copy_node.next
                head = head.next
            else:
                copy_node.next = None
                copy_node = copy_node.next
                break

        while copy_node_1:
            copy_list.append(copy_node_1)  # 遍历 copy_node,存储所有节点
            copy_node_1 = copy_node_1.next

        copy_list.append(copy_node)  # 这里加入最后节点 None

        ln = len(copy_list)

        for i in range(ln-1):
            if random_list[i] == None:  # random 是 None，指向 最后一个 copy_node
                copy_list[i].random = copy_list[-1]
            else:
                # 查找 random 在 head_list 里的 index
                j = head_list.index(random_list[i])
                # 将 copy_node.random = copy_list 中对应位置 index 的值
                copy_list[i].random = copy_list[j]
        return rev
