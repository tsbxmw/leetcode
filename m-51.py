# 面试题51. 数组中的逆序对
# 在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。


# 示例 1:

# 输入: [7,5,6,4]
# 输出: 5


# 限制：

# 0 <= 数组长度 <= 50000

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        # 使用 动态规划
        if not nums:
            return 0
        dp = [0 for _ in nums]
        ln = len(nums)

        i = 1
        while i < ln:
            j = 0
            while j < i:
                if nums[i] < nums[j]:
                    dp[i] += dp[j]
                i += 1
            i += 1

        return sum(dp)
