# 给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。

# 请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

# 你可以假设 nums1 和 nums2 不会同时为空。

# 示例 1:

# nums1 = [1, 3]
# nums2 = [2]

# 则中位数是 2.0
# 示例 2:

# nums1 = [1, 2]
# nums2 = [3, 4]

# 则中位数是 (2 + 3)/2 = 2.5

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/median-of-two-sorted-arrays
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


## 合并后再计算

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = []
        l1 = len(nums1)
        l2 = len(nums2)

        i = j = 0
        while i < l1 and j < l2:
            if nums1[i] <= nums2[j]:
                nums3.append(nums1[i])
                i += 1
            else:
                nums3.append(nums2[j])
                j += 1
        nums3.extend(nums1[i:])
        nums3.extend(nums2[j:])

        mid = (l1+l2) // 2
        if (l1+l2)%2 == 0:
            return (nums3[mid] + nums3[mid-1])/2
        else:
            return nums3[mid]

            

