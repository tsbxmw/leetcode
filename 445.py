# 445.
# 两数相加
# II
# 给定两个非空链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储单个数字。将这两数相加会返回一个新的链表。
#
#
#
# 你可以假设除了数字
# 0
# 之外，这两个数字都不会以零开头。
#
# 进阶:
#
# 如果输入链表不能修改该如何处理？换句话说，你不能对列表中的节点进行翻转。
#
# 示例:
#
# 输入: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出: 7 -> 8 -> 0 -> 7

# https://leetcode-cn.com/problems/add-two-numbers-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1.val == 0:
            return l2
        if l2.val == 0:
            return l1

        v1 = v2 = ''

        while l1:
            v1 += str(l1.val)
            l1 = l1.next
        while l2:
            v2 += str(l2.val)
            l2 = l2.next

        v3 = str(int(v1) + int(v2))
        lenv = len(v3) - 1

        rev = l3 = ListNode(0)
        for i, x in enumerate(v3):
            l3.val = int(x)
            if i == lenv:
                break
            l3.next = ListNode(0)
            l3 = l3.next

        return rev
