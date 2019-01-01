class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        tmp=set([])
        i=0
        best=0
        while (i<len(s)):
            best = max(best,1)
            tmp.clear();
            j=i+1
            tmp.add(s[i])
            while (j<len(s)):
                if (s[j] in tmp):
                    if (best<(j-i)):
                        best=j-i;
                    break;
                else:
                    best=max(best,j-i+1)
                    tmp.add(s[j])
                    j=j+1
            i=i+1
        return best
