class Solution:
    def isPalindrome(self, s: str) -> bool:
        my_string = "".join(c.lower() for c in s if c.isalnum())
        i = 0
        j = len(my_string)-1
        while i<j:
            if my_string[i]== my_string[j]:
                i+=1
                j-=1
                continue
            else:
                return False
        return True
        
        