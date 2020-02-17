# 给出一个区间的集合，请合并所有重叠的区间。

# 示例 1:

# 输入: [[1,3],[2,6],[8,10],[15,18]]
# 输出: [[1,6],[8,10],[15,18]]
# 解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
# 示例 2:

# 输入: [[1,4],[4,5]]
# 输出: [[1,5]]
# 解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/merge-intervals
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ln = len(intervals)
        if ln == 0:
            return []
        rev = []
        intervals.sort(key=lambda x: x[0])
        for i, x in enumerate(intervals):
            if i == 0:
                rev.append(x)
            else:
                if rev[-1][1] >= x[0]:
                    rev[-1][1] = max(rev[-1][1], x[1])
                else:
                    rev.append(x)
        return rev
