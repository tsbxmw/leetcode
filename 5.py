# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

# 示例 1：

# 输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
# 示例 2：

# 输入: "cbbd"
# 输出: "bb"

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/longest-palindromic-substring
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

## 动态规划

class Solution:
    def longestPalindrome(self, s: str) -> str:
        ls = len(s)
        revmax = ""
        longcount = 0
        dp = [[0] * ls for i in range(ls) ]

        for i in range(ls):
            for j in range(i+1):
                if i - j <= 1:
                    if s[i] == s[j]:
                        dp[j][i] = 1
                        temp = i-j+1
                        if temp > longcount:
                            longcount = temp
                            revmax = s[j:i+1]
                else:
                    if s[i] == s[j] and dp[j+1][i-1]:
                        dp[j][i] = 1
                        temp = i-j+1
                        if temp>longcount:
                            longcount = temp
                            revmax = s[j:i+1]
        return revmax

if __name__ == "__main__":
    s = Solution()
    print(s.longestPalindrome("abacaba"))
    print(s.longestPalindrome("abaacaba"))
    print(s.longestPalindrome("abacabaaaa"))
    print(s.longestPalindrome("abacaaabaaa"))