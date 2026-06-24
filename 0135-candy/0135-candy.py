class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        leftSum=[0]*len(ratings)
        leftSum[0] = 1
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                leftSum[i] = leftSum[i-1]+1
            else:
                leftSum[i] = 1
        print(leftSum)
        # sum=leftSum[len(ratings)-1]
        sum=max(1, leftSum[len(ratings)-1])
        print(sum)
        prev=1
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                curr=prev+1
            else:
                curr=1
            prev = curr
            sum+=max(leftSum[i], curr)
        return sum

        