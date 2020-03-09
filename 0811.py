class Solution:
    def waysToChange(self, n: int) -> int:
        temp = [1, 5, 10, 25]
        dp = [[0 for i in range(4)] for i in range(n+1)]
        dp[1][0] = 1
        dp[0][0] = 1
        for i in range(2, n+1):


            for j, x in enumerate(temp):
                if i > x:
                    temp_j = 0
                    while temp_j <= j:
                        dp[i][j] += dp[i-x][temp_j]
                        temp_j += 1
                elif i==x:
                    dp[i][j] += 1
                    break
        return sum(dp[n])


if __name__ == "__main__":
    s = Solution()
    print(s.waysToChange(50))