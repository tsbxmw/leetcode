# 14. 最长公共前缀
# 编写一个函数来查找字符串数组中的最长公共前缀。

# 如果不存在公共前缀，返回空字符串 ""。

# 示例 1:

# 输入: ["flower","flow","flight"]
# 输出: "fl"
# 示例 2:

# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
# 说明:

# 所有输入只包含小写字母 a-z 。

class Solution:
    def longestCommonPrefix(self, strs) -> str:
        ls = len(strs)
        if ls == 0:
            return ''
        if ls == 1:
            return strs[0]

        strs.sort(key=lambda x: len(x))
        temp = strs[0]
        lt = len(temp)

        if lt == 0:
            return ''
        i = 0
        
        flag = False
        while i < lt:
            for s in strs[1:]:
                if s[i] == temp[i]:
                    continue
                else:
                    flag = True
                    break
            if flag:
                break
            else:
                i+=1
        
        if not flag:
            return temp
        if i == 0:
            return ''
        return temp[:i]
            
            
if __name__ == "__main__":
    s = Solution()
    print(s.longestCommonPrefix(["flower","flow","flight"]))
    print(s.longestCommonPrefix(["dog","racecar","car"]))
    print(s.longestCommonPrefix(["","racecar","car"]))
    print(s.longestCommonPrefix(["dog","dog"]))
    print(s.longestCommonPrefix(["cd", "cc"]))