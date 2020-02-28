# 143. 重排链表
# 给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
# 将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…

# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

# 示例 1:

# 给定链表 1->2->3->4, 重新排列为 1->4->2->3.
# 示例 2:

# 给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3.


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

## 整体上是交换，使用递归，先找到最后节点
## 1 -》 2 -》 3 -》 4 -》 5
## |                |
## temp = 1.next == 2
## 1.next = 4.next == 5
## 4.next = None
## 1.next.next == 5.next = 2
## now = 2
## last = 3.next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        self.pre = head
        self.flag = True
        def test(node):
            if not node.next:  # 如果 node.next 是 None，就不需要交换了
                return
            test(node.next)
            if not self.flag:
                return
            
            if not self.pre.next:
                self.flag = False
                return 
            if self.pre == node:
                self.flag = False
                return 
            temp = self.pre.next
            self.pre.next = node.next
            self.pre.next.next = temp
            self.pre = temp
            node.next = None

        test(self.pre)