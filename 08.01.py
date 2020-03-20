# 面试题 08.01. 三步问题
# 三步问题。有个小孩正在上楼梯，楼梯有n阶台阶，小孩一次可以上1阶、2阶或3阶。实现一种方法，计算小孩有多少种上楼梯的方式。结果可能很大，你需要对结果模1000000007。

# 示例1:

#  输入：n = 3
#  输出：4
#  说明: 有四种走法
# 示例2:

#  输入：n = 5
#  输出：13
# 提示:

# n范围在[1, 1000000]之间


class Solution:
    data = [1, 1, 2, 4]

    def waysToStep(self, n: int) -> int:

        mod_num = 1000000007

        rev = 0
        t0 = 0
        t1 = 1
        t2 = 2
        t3 = 4

        if n == 0:
            return 0
        if n == 1:
            return t1
        if n == 2:
            return t2
        if n == 3:
            return t3
        ld = len(self.data)
        if n < ld:
            return self.data[n]

        i = ld
        while i <= n:
            self.data.append(
                (self.data[i-1] + self.data[i-2] + self.data[i-3]) % mod_num)
            i += 1

        return self.data[n] % mod_num

