# 300. 最长上升子序列
# 给定一个无序的整数数组，找到其中最长上升子序列的长度。

# 示例:

# 输入: [10,9,2,5,3,7,101,18]
# 输出: 4
# 解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
# 说明:

# 可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
# 你算法的时间复杂度应该为 O(n2) 。
# 进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?


# 双层 dp， O(n^2)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ln = len(nums)
        if ln == 0:
            return 0
        dp = [1 for i in range(ln)]

        for i in range(ln):
            j = 0
            while j < i:
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
                j += 1
        return max(dp)
