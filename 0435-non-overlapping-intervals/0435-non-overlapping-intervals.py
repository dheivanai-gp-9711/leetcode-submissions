class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda i:i[1])
        prevEnd = intervals[0][1]
        count=1#consider first interval as non overlapping one
        for i in range(1, len(intervals)):
            if intervals[i][0] >= prevEnd:
                count+=1
                prevEnd = intervals[i][1]
        return len(intervals) - count