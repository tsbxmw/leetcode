# 912. 排序数组
# 给你一个整数数组 nums，将该数组升序排列。


# 示例 1：

# 输入：nums = [5,2,3,1]
# 输出：[1,2,3,5]
# 示例 2：

# 输入：nums = [5,1,1,2,0,0]
# 输出：[0,0,1,1,2,5]


# 提示：

# 1 <= nums.length <= 50000
# -50000 <= nums[i] <= 50000

class Solution:
    def sortArray(self, nums):

        def quick_sort(left, right):
            if left >= right:
                return
            target = nums[left]
            i = left
            j = right
            while i < j:
                while i < j and nums[j] >= target:
                    j -= 1
                nums[i] = nums[j]
                while i < j and nums[i] < target:
                    i += 1
                nums[j] = nums[i]
            nums[i] = target
            quick_sort(left, i - 1)
            quick_sort(i+1, right)
        quick_sort(0, len(nums)-1)


if __name__ == "__main__":
    s = Solution()
    s.sortArray([1, 3, 2, 4, 1, 5, 6, 1, 10, 9, 2, 4, 6])
