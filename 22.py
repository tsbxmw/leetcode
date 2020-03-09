# 22. 括号生成
# 给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

# 例如，给出 n = 3，生成结果为：

# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]
# 通过次数77,024提交次数104,902


# 我觉得是 深度搜索
class Solution:
    def generateParenthesis(self, n: int):
        if n == 0:
            return []
        if n == 1:
            return ["()"]
        self.rev = []

        def dfs(temp, left_count, right_count):
            if left_count > right_count:
                return
            if left_count > 0:
                dfs(temp+"(", left_count-1, right_count)
            if right_count > 0:
                dfs(temp+")", left_count, right_count-1)
            if left_count == right_count == 0:
                self.rev.append(temp)

        dfs("", n, n)
        return self.rev


if __name__ == "__main__":
    s = Solution()
    print(s.generateParenthesis(10))
        