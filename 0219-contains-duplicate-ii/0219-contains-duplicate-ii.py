class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        map=set()
        windowSize = k
        for i, val in enumerate(nums):
            if val in map:
                return True
            map.add(val)
            if len(map) > k:
                map.remove(nums[i-k])
            
            
        return False
            

        