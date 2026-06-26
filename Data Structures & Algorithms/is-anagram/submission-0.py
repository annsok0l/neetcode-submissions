class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        answer = False
        if Counter(s)== Counter(t):
            answer = True
        return answer
        