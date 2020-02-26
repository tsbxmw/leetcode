# 32. 最长有效括号
# 给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。
#
# 示例 1:
#
# 输入: "(()"
# 输出: 2
# 解释: 最长有效括号子串为 "()"
# 示例 2:
#
# 输入: ")()())"
# 输出: 4
# 解释: 最长有效括号子串为 "()()"

# 感觉是动态规划，使用以当前字符结尾的最长长度
# dp[0] = 0
# dp[1] = 2 if s[0]=='(' and s[1]==')' else 0
# 主要考虑到有这种情况 ( ) ( ( ) )
#                   0 1 2 3 4 5
# 这是候要将  1 位置的数据也要加进去
# 所以当 5 位置组合成了一个 > 0 的组合时，要将 dp[1] 的长度也加进去
# 既 dp[i] = dp[i-1] + 2       +   dp[i-dp[i-1]-2]
#           多了一对 前面的 + 2，   这里是 匹配成功的字符的前一个字符的长度值，也要加进来


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        ls = len(s)
        if ls == 0 or ls == 1:
            return 0

        dp = [0 for _ in s]

        for i in range(1, ls):
            if i-dp[i-1]-1 < 0:
                continue
            if s[i] == ')' and s[i-dp[i-1]-1] == '(':
                dp[i] = dp[i-1] + 2 + dp[i-dp[i-1]-2]

        return max(dp)


if __name__ == "__main__":
    s = Solution()
    print(s.longestValidParentheses("(()"))
    print(s.longestValidParentheses(")()())"))
    print(s.longestValidParentheses("(((())))))))"))
    print(s.longestValidParentheses("()()()()()()"))
    print(s.longestValidParentheses("()(())"))
    print(s.longestValidParentheses("(()))())("))
