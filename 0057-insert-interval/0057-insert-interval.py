class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        result=[]
        # if len(intervals) == 0:
        #     result.append(newInterval)
        #     return result
        n=len(intervals)
        
        i=0
        # while i<n:
        #     if intervals[i][1] < newInterval[0]:#i havent touched the start yet.
        #         result.append(intervals[i])
        #         i+=1
        #     elif newInterval[1] >= intervals[i][0]:
        #         while i<n and newInterval[1] >= intervals[i][0]:
        #             newInterval[0] = min(newInterval[0], intervals[i][0])
        #             newInterval[1] = max(newInterval[1], intervals[i][1])
        #             i+=1 
        #         result.append(newInterval)
        #     else:
        #         result.append(intervals[i])
        #         i+=1
        while i<n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i+=1
        while i<n and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i+=1 
        result.append(newInterval)
        while i<n:
            result.append(intervals[i])
            i+=1
        return result