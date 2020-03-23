# 面试题24. 反转链表
# 定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。


# 示例:

# 输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL


# 限制：

# 0 <= 节点个数 <= 5000


# 注意：本题与主站 206 题相同：https://leetcode-cn.com/problems/reverse-linked-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        self.rev = None

        def dfs(node):
            if node and not node.next:
                self.rev = node
                return node
            a = dfs(node.next)
            node.next = None
            a.next = node
            return node

        dfs(head)
        return self.rev


class Solution1:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        if not head.next:
            return head
        rev = None
        current = head

        while current:
            temp = current.next
            current.next = rev
            rev = current
            current = temp
        return rev


if __name__ == "__main__":
    s = Solution()
    a = ListNode(0)
    a1 = ListNode(1)
    a2 = ListNode(2)
    a3 = ListNode(3)
    a4 = ListNode(4)
    a.next = a1
    a1.next = a2
    a2.next = a3
    a3.next = a4
    # while a:
    #     print(a.val)
    #     a = a.next
    # b = s.reverseList(a)
    # while b:
    #     print(b.val)
    #     b = b.next
    s1 = Solution1()
    b = s1.reverseList(a)
    while b:
        print(b.val)
        b = b.next
