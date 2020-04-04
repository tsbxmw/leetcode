# 29. 两数相除
# 给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。

# 返回被除数 dividend 除以除数 divisor 得到的商。

# 整数除法的结果应当截去（truncate）其小数部分，例如：truncate(8.345) = 8 以及 truncate(-2.7335) = -2


# 示例 1:

# 输入: dividend = 10, divisor = 3
# 输出: 3
# 解释: 10/3 = truncate(3.33333..) = truncate(3) = 3
# 示例 2:

# 输入: dividend = 7, divisor = -3
# 输出: -2
# 解释: 7/-3 = truncate(-2.33333..) = -2


# 提示：

# 被除数和除数均为 32 位有符号整数。
# 除数不为 0。
# 假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。本题中，如果除法结果溢出，则返回 231 − 1。
# 通过次数41,132提交次数211,740

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor == 0:
            return 0
        if dividend == 0:
            return 0

        flag = False
        if divisor < 0:
            flag = True
            divisor = -divisor
        if dividend < 0:
            flag = not flag
            dividend = -dividend

        def div(a, b):
            if a < b:
                return 0
            if a == b:
                return 1
            count = 1
            temp = b
            while (temp+temp) <= a:
                temp += temp
                count += count
            count += div(a-temp, b)
            return count
        rev = div(dividend, divisor)
        if flag:
            rev = -rev
        if rev <= -2147483648:
            return -2147483648
        elif rev >= 2147483647:
            return 2147483647
        return rev
