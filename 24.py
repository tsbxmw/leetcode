# 24. 两两交换链表中的节点
# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。


# 示例:

# 给定 1->2->3->4, 你应该返回 2->1->4->3.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:

        def reverse2node(node):
            pre = None
            while node:
                nex = node.next
                node.next = pre
                pre = node
                node = nex
            return pre

        if not head:
            return None
        trev = rev = ListNode(0)
        begin = tail = head
        while True:
            n = 2
            while tail and n:
                tail = tail.next
                n -= 2
            if n > 0 or not tail:
                rev.next = head
                break
            temp = tail.next
            tail.next = None
            rev.next = reverse2node(head)
            rev = head
            head = temp
            tail = temp
        return trev.next
