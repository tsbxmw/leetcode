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


# 我觉得是 深度搜索加剪枝
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        start = "(" * n + ""

        