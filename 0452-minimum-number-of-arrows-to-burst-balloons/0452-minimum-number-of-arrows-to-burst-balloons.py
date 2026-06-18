class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort(key=lambda i:i[0])
        count=1
        overlap=points[0]
        for i in range(1, len(points)):
            if points[i][0] <= overlap[1]:
                overlap=[points[i][0], min(overlap[1], points[i][1])]
            else:
                count+=1
                overlap=points[i]
        return count
        