class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if len(intervals) == 0:
            return 0
        if len(intervals) == 1:
            return 0
        intervals.sort(key=lambda val:val[1])
        # print(intervals)
        currTime = intervals[0][1]
        count=1

        for i in range(1, len(intervals)):
            if intervals[i][0] >= currTime:
                count+=1
                currTime = intervals[i][1]
        return len(intervals) - count
        