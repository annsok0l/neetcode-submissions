class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        res=0
        l=0
        count = {}
        for r in range(len(s)):
            count[s[r]] = 1+ count.get(s[r],0)
            max_len = max(max_len, count[s[r]])
            while (r-l+1)- max_len>k:
                count[s[l]]-=1
                l+=1
            res = max(res,r-l+1)
            
        return res



         