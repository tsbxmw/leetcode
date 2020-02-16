# 给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。

# k 是一个正整数，它的值小于或等于链表的长度。

# 如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

# 示例 :

# 给定这个链表：1->2->3->4->5

# 当 k = 2 时，应当返回: 2->1->4->3->5

# 当 k = 3 时，应当返回: 3->2->1->4->5

# 说明 :

# 你的算法只能使用常数的额外空间。
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/reverse-nodes-in-k-group
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


## 先取值再重新生成新的 ListNode

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        temp = []
        while head:
            temp.append(head.val)
            head = head.next
        lt = len(temp)

        rev = l = ListNode(0)
        tt = []
        i = 0
        while i+k <= lt: ## 这里判断 i+k <= lt 才可以翻转
            tt.extend(temp[i:i+k][::-1])   
            i += k
        if lt > len(tt):  ##这里判断 如果没遍历完，把后面的加进去
            tt.extend(temp[i:])
        for x in tt:
            l.next = ListNode(x)
            
            l = l.next
        return rev.next

