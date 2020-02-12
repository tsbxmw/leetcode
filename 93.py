# 给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。

# 示例:

# 输入: "25525511135"
# 输出: ["255.255.11.135", "255.255.111.35"]

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/restore-ip-addresses
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

## 回溯即可
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        self.ans = []
        def test(s, temp):
            if len(temp) > 4:
                return
            if not s:
                if len(temp) == 4:
                    self.ans.append(".".join(temp))
                return
            val = ""
            for i, x in enumerate(s):
                if val.startswith('0'):
                    temp.append(val)
                    test(s[i:], temp[::])
                    val = x
                    continue
                val += x
                if int(val) <= 255:
                    temp.append(val)
                    test(s[i+1:], temp[::])
                    temp.pop()
                else:
                    return
        test(s, [])
        return list(set(self.ans))
