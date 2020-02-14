# 反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

# 说明:
# 1 ≤ m ≤ n ≤ 链表长度。

# 示例:

# 输入: 1->2->3->4->5->NULL, m = 2, n = 4
# 输出: 1->4->3->2->5->NULL

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/reverse-linked-list-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


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
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        rev = head
        i = 0
        if m >= 2:
            while i<m-2:
                head = head.next
                i += 1
            pre = head
            head = head.next
            i+=1
        else:
            pre = head
        temp = None
        while head and i < n:
            a = head.next
            head.next = temp
            temp = head
            head = a
            i+=1

        if m == 1:
            pre = temp
            while temp.next:
                temp = temp.next
            temp.next = head
            return pre
        else:

            pre.next = temp

            while pre.next:
                pre = pre.next
            pre.next=head
            return rev