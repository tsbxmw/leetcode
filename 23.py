# 合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

# 示例:

# 输入:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# 输出: 1->1->2->3->4->4->5->6

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/merge-k-sorted-lists
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


## 根据合并 2 个有序链表，笨的办法就是下面的方法，将当前的所有的值的最小值进链表，并向后迭代。
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        l = rev = ListNode(0)
        ll = len(lists)
        if ll == 0:
            return None
        if ll == 1:
            return lists[0]


        while any(lists):
            temp = min([x.val for x in lists if x])
            for i, ltemp in enumerate(lists):
                if ltemp:
                    if ltemp.val == temp:
                        l.next = ListNode(temp)
                        lists[i] = lists[i].next
                        l = l.next
        return rev.next