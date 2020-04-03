# 面试题 02.05. 链表求和
# 给定两个用链表表示的整数，每个节点包含一个数位。

# 这些数位是反向存放的，也就是个位排在链表首部。

# 编写函数对这两个整数求和，并用链表形式返回结果。


# 示例：

# 输入：(7 -> 1 -> 6) + (5 -> 9 -> 2)，即617 + 295
# 输出：2 -> 1 -> 9，即912
# 进阶：假设这些数位是正向存放的，请再做一遍。

# 示例：

# 输入：(6 -> 1 -> 7) + (2 -> 9 -> 5)，即617 + 295
# 输出：9 -> 1 -> 2，即912


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# 计算每个值，相加生成新的 node# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        rev = l3 = ListNode(0)

        temp = 0
        while (l1 and l1.next) or (l2 and l2.next):
            count = 0
            if l1:
                count += l1.val
                l1 = l1.next
            if l2:
                count += l2.val
                l2 = l2.next
            count += temp
            temp = 0
            if count >= 10:
                count -= 10
                temp = 1
            rev.val = count
            rev.next = ListNode(0)
            rev = rev.next

        count = 0
        if l1:
            count += l1.val
        if l2:
            count += l2.val
        count += temp
        if count >= 10:
            rev.val = count - 10
            rev.next = ListNode(1)
        else:
            rev.val = count
        return l3
