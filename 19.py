# 19. 删除链表的倒数第N个节点
# 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

# 示例：

# 给定一个链表: 1->2->3->4->5, 和 n = 2.

# 当删除了倒数第二个节点后，链表变为 1->2->3->5.
# 说明：

# 给定的 n 保证是有效的。

# 进阶：

# 你能尝试使用一趟扫描实现吗？

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if n == 0:
            return head
        temp = [ListNode(0)]
        pre = temp[0]
        pre.next = head
        while head:
            temp.append(head)
            head = head.next
        temp.append(None)
        ln = len(temp)
        if ln == 2:
            return None

        temp[ln-n-2].next = temp[ln-n]
        return pre.next

# 双指针


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:
            return None
        dummy = ListNode(0)
        dummy.next = head
        temp = []
        # 双指针
        pre = tail = dummy

        while tail and n >= 0:
            tail = tail.next
            n -= 1

        while pre and tail:
            pre = pre.next
            tail = tail.next
        pre.next = pre.next.next
        return dummy.next
