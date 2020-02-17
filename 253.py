# 给定一个会议时间安排的数组，每个会议时间都会包括开始和结束的时间 [[s1,e1],[s2,e2],...] (si < ei)，为避免会议冲突，同时要考虑充分利用会议室资源，请你计算至少需要多少间会议室，才能满足这些会议安排。

# 示例 1:

# 输入: [[0, 30],[5, 10],[15, 20]]
# 输出: 2
# 示例 2:

# 输入: [[7,10],[2,4]]
# 输出: 1

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/meeting-rooms-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        ln = len(intervals)
        if ln == 0:
            return 0
        rev = []
        intervals.sort(key=lambda x: x[0])
        for i, x in enumerate(intervals):
            if i >= 0:
                flag = False
                for j, t in enumerate(rev):
                    if t[1] <= x[0]:
                        rev[j] = x[::]
                        flag = True
                        break
                if not flag:
                    rev.append(x)
            else:
                rev.append(x)

        return len(rev)