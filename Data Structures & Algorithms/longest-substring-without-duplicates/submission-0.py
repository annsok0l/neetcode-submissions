class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        start = 0
        mp = {}

        for end in range(len(s)):
            if s[end] in mp:
                start = max(mp[s[end]]+1,start)
            mp[s[end]] = end
            max_length = max(max_length, end-start+1)
        
        return max_length
                



