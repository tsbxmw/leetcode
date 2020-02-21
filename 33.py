# 33. 搜索旋转排序数组
# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。

# ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

# 搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

# 你可以假设数组中不存在重复的元素。

# 你的算法时间复杂度必须是 O(log n) 级别。

# 示例 1:

# 输入: nums = [4,5,6,7,0,1,2], target = 0
# 输出: 4
# 示例 2:

# 输入: nums = [4,5,6,7,0,1,2], target = 3
# 输出: -1

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ln = len(nums)
        if ln == 0:
            return -1
        
        def test(s, e):
            if s>=e:
                return -1
            
            mid = (s+e) // 2
            
            if nums[mid] > nums[mid+1]:
                return mid
            l = test(s, mid)
            r = test(mid+1, e)
            if l != -1:
                return l
            else:
                return r
            
        result = test(0, ln-1)
        
        def searchnum(s, e, target):
            if s>e:
                return -1
            mid = (s+e)//2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                return searchnum(s, mid-1, target)
            else:
                return searchnum(mid+1, e, target)
        
        if target > nums[result]:
            return -1
        if result == -1:
            return searchnum(0, ln-1, target)
        elif nums[result+1] <= target <= nums[ln-1]:
            return searchnum(result+1, ln-1, target)
        else:
            return searchnum(0, result, target)
        