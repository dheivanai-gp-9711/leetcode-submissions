class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        smap={}
        k = len(p)
        pmap = Counter(p)
        if k > len(s):
            return []
        for i in range(k):
            if s[i] in smap:
                smap[s[i]]+=1
            else:
                smap[s[i]]=1
        result=[]
        if pmap==smap:
            result.append(0)
        i=k
        while i<len(s):
            if s[i] in smap:
                smap[s[i]]+=1
            else:
                smap[s[i]]=1
            # if len(smap) > k:
            if smap[s[i-k]] == 1:
                del smap[s[i-k]]
            else:
                smap[s[i-k]]-=1
            if smap == pmap:
                result.append(i-k+1)
            i+=1
        return result
        