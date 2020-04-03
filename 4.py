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


# 合并后再计算


class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
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
        if (l1+l2) % 2 == 0:
            return (nums3[mid] + nums3[mid-1])/2
        else:
            return nums3[mid]


# 假合并
class Solution2:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        # 排序
        l1 = len(nums1)
        l2 = len(nums2)

        mid = 0
        if (l1+l2) % 2 == 0:
            mid = (l1+l2)//2 - 1
            i = j = 0
            temp = []
            while i < l1 and j < l2:
                if i+j in (mid, mid+1):
                    temp.append(min(nums1[i], nums2[j]))
                if i+j > mid+1:
                    return sum(temp)/2
                if nums1[i] < nums2[j]:
                    i += 1
                else:
                    j += 1
            while i < l1:
                if i+j in (mid, mid+1):
                    temp.append(nums1[i])
                if i+j >= mid+1:
                    return sum(temp)/2
                i += 1
            while j < l2:
                if i+j in (mid, mid+1):
                    temp.append(nums2[j])
                if i+j >= mid+1:
                    return sum(temp)/2
                j += 1
        else:
            mid = (l1+l2)//2
            i = j = 0
            while i < l1 and j < l2:
                if i+j == mid:
                    return min(nums1[i], nums2[j])

                if nums1[i] < nums2[j]:
                    i += 1
                else:
                    j += 1
            while i < l1:
                if i+j == mid:
                    return nums1[i]
                i += 1
            while j < l2:
                if i+j == mid:
                    return nums2[j]
                j += 1


# log(m+n), 第 k 小数

class Solution3:
    def findMedianSortedArrays(self, nums1, nums2) -> float:

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        len1, len2 = len(nums1), len(nums2)

        left, right, half_len = 0, len1, (len1 + len2 + 1) // 2
        mid1 = (left + right) // 2
        mid2 = half_len - mid1

        while left < right:
            if mid1 < len1 and nums2[mid2-1] > nums1[mid1]:
                left = mid1 + 1
            else:
                right = mid1
            mid1 = (left + right) // 2
            mid2 = half_len - mid1

        if mid1 == 0:
            max_of_left = nums2[mid2-1]
        elif mid2 == 0:
            max_of_left = nums1[mid1-1]
        else:
            max_of_left = max(nums1[mid1-1], nums2[mid2-1])

        if (len1 + len2) % 2 == 1:
            return max_of_left

        if mid1 == len1:
            min_of_right = nums2[mid2]
        elif mid2 == len2:
            min_of_right = nums1[mid1]
        else:
            min_of_right = min(nums1[mid1], nums2[mid2])

        return (max_of_left + min_of_right) / 2


class Solution4(object):
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        l1 = len(nums1)
        l2 = len(nums2)

        if l1 > l2:
            nums1, nums2, l1, l2 = nums2, nums1, l2, l1
        k = (l1+l2+1)//2

        def get_mid(nums1, s1, e1, nums2, s2, e2, k):
            current_l1 = e1 - s1 + 1
            current_l2 = e2 - s2 + 1

            if current_l1 > current_l2:
                return get_mid(nums2, s2, e2, nums1, s1, e1, k)
            if current_l1 == 0:
                return nums2[s2 + k - 1]
            if k == 1:
                return min(nums1[s1], nums2[s2])

            i = s1 + min(current_l1, k // 2) - 1
            j = s2 + min(current_l2, k // 2) - 1

            if nums1[i] < nums2[j]:
                return get_mid(nums1, s1 + k//2, e1, nums2, s2, e2, k - k // 2)
            else:
                return get_mid(nums1, s1, e1, nums2, s2 + k//2, e2, k - k // 2)
        return get_mid(nums1, 0, l1-1, nums2, 0, l2-1, k)


if __name__ == "__main__":
    s3 = Solution4()
    a = s3.findMedianSortedArrays([1, 3], [2])
    print(a)
