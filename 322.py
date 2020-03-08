# 322. 零钱兑换
# 给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

# 示例 1:

# 输入: coins = [1, 2, 5], amount = 11
# 输出: 3 
# 解释: 11 = 5 + 5 + 1
# 示例 2:

# 输入: coins = [2], amount = 3
# 输出: -1
# 说明:
# 你可以认为每种硬币的数量是无限的。



class Solution:
    def coinChange(self, coins, amount: int) -> int:
        coins.sort()
        dp = [0 for _ in range(amount+1)]
        dp[0] = 0

        for i in range(1, amount+1):
            temp = []
            for j in coins:
                if i - j == 0:
                    temp.append(0)
                    break
                elif i - j < 0:
                    break
                else:
                    if dp[i-j] >= 0:
                        temp.append(dp[i-j])
            if temp:
                dp[i] = min(temp) + 1
            else:
                dp[i] = -1
        return dp[amount]

if __name__ == "__main__":
    s = Solution()
    print(s.coinChange([1,2,5,10,14], 1000))

    print(72)

    