# 61. 旋转链表
# 给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。

# 示例 1:

# 输入: 1->2->3->4->5->NULL, k = 2
# 输出: 4->5->1->2->3->NULL
# 解释:
# 向右旋转 1 步: 5->1->2->3->4->NULL
# 向右旋转 2 步: 4->5->1->2->3->NULL
# 示例 2:

# 输入: 0->1->2->NULL, k = 4
# 输出: 2->0->1->NULL
# 解释:
# 向右旋转 1 步: 2->0->1->NULL
# 向右旋转 2 步: 1->2->0->NULL
# 向右旋转 3 步: 0->1->2->NULL
# 向右旋转 4 步: 2->0->1->NULL

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 挺简单的，只需要计算出要位移的数字即可。
# 也可以首尾相连，遍历 k-1次后断开即可。

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or k == 0:
            return head
        pre = temp = head
        count = 0
        while pre:
            count += 1
            if pre.next:
                pre = pre.next
            else:
                break
        

        k = count - k%count
        if k == 0:
            return head
        else:
            pre.next = head
        while k > 1:
            head = head.next
            k -= 1
        rev = head.next
        head.next = None
        return rev




