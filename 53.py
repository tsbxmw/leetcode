# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

# 示例:

# 输入: [-2,1,-3,4,-1,2,1,-5,4],
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/maximum-subarray
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

## 动态规划： dp[i] 表示以 i 位置为结尾的子串的最大值， 每次更新 dp[i]=max(dp[i-1]+nums[i], nums[i])

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ln = len(nums)

        if ln == 1:
            return nums[0]
        
        dp = [0 for i in nums]
        dp[0] = nums[0]
        for i in range(1, ln):
            dp[i] = max(nums[i], nums[i]+dp[i-1])
        
        return max(dp)

