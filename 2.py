# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

# 示例：

# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/add-two-numbers
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


## 计算数字，相加，生成新的列表

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        nums1 = nums2 = 0
        i = j = 0
        while l1:
            nums1 += l1.val * (10 ** i)
            l1 = l1.next
            i += 1
        
        while l2:
            nums2 += l2.val * (10 ** j)
            l2 = l2.next
            j += 1
        result = nums1 + nums2

        rev = temp = ListNode(0)

        for i in str(result)[::-1]:
            temp.next = ListNode(int(i))
            temp = temp.next

        return rev.next


## 各位相加，进位生成新的链表

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        rev = l3 = ListNode(0)
        flag = 0
        while l1 or l2:
            temp = 0
            if l1:
                temp += l1.val
                l1 = l1.next
            if l2:
                temp += l2.val
                l2 = l2.next
            temp += flag
            if temp >= 10:
                flag = 1
                temp -= 10
            else:
                flag = 0
            l3.next = ListNode(temp)
            l3 = l3.next
        if flag == 1:
            l3.next = ListNode(1)
        return rev.next
