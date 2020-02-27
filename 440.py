# 给定整数 n 和 k，找到 1 到 n 中字典序第 k 小的数字。

# 注意：1 ≤ k ≤ n ≤ 109。

# 示例 :

# 输入:
# n: 13   k: 2

# 输出:
# 10

# 解释:
# 字典序的排列是 [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]，所以第二小的数字是 10。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/k-th-smallest-in-lexicographical-order
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


## 思路： 遍历 10 叉树，再把树相关代码删除即可。
class Solution1:
    def findKthNumber(self, n: int, k: int) -> int:
        # class TreeNode:
        #     def __init__(self, val):
        #        self.val = val
        #        self.others = []
        #
        #     def __str__(self):
        #         self.test(self)
        #         return ''
        #
        #     def test(self, temp):
        #         if not temp:
        #             return
        #         print(temp.val)
        #         for i in temp.others:
        #             self.test(i)
        #
        # root = TreeNode(0)
        floor = len(str(n))
        self.count = 1
        self.val = 0

        def test(val, f):
            if val > n:
                return None
            if self.count == k:
                self.val = val
                return val

            #temp = TreeNode(val)
            self.count += 1
            # print(val, f, self.count)
            for i in range(10):
                test(val * 10 + i, f + 1)
                if self.val != 0:
                    return
                #temp.others.append(x)
            #return temp

        for i in range(1, 2):
            if self.val != 0:
                return self.val
            test(i, 0)
        return self.val


## 上面的超时，下面的使用的是计算总数：上面的是每次1累加
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:

        def get_count_of_now(now):
            print(now)
            next = now+1
            temp_n = n+1
            count = 0
            while now < temp_n:
                count += min(temp_n, next) - now
                now *= 10
                next *= 10
            return count

        now = 1
        while k>0:
            count = get_count_of_now(now)
            if count >= k:
                k -= 1
                if k == 0:
                    return now
                now *= 10
            elif count < k:
                k -= count
                if k == 0:
                    return now
                now += 1
        return now


if __name__ == "__main__":
    s = Solution()
    print(s.findKthNumber(9999, 1110))
    s1 = Solution1()
    print(s1.findKthNumber(9999, 1110))