# 给定一个会议时间安排的数组，每个会议时间都会包括开始和结束的时间 [[s1,e1],[s2,e2],...] (si < ei)，请你判断一个人是否能够参加这里面的全部会议。

# 示例 1:

# 输入: [[0,30],[5,10],[15,20]]
# 输出: false
# 示例 2:

# 输入: [[7,10],[2,4]]
# 输出: true

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/meeting-rooms
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        ln = len(intervals)
        if ln == 0:
            return True
        rev = []
        intervals.sort(key=lambda x: x[0])
        for i, x in enumerate(intervals):
            if i == 0:
                rev = x[::]
            else:
                if rev[1] > x[0]:
                    return False
                else:
                    rev = x[::]
        return True