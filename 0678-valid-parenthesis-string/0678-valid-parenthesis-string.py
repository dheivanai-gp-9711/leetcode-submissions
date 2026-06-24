class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        min=0
        max=0
        for c in s:
            if c == '(':
                min+=1
                max+=1
            elif c == ')':
                min-=1
                max-=1
            else:
                min-=1
                max+=1
            if min < 0:
                min=0
            if max<0:
                return False
        return True if min == 0 else False
        