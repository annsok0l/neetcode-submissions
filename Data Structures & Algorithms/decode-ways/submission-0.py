class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        
        n = len(s)
        # dp[i] stores the number of decodings for substring s[:i]
        dp = [0] * (n + 1)
        
        # Base cases
        dp[0] = 1  # An empty string has 1 valid way
        dp[1] = 1  # First char is guaranteed non-zero by check above
        
        for i in range(2, n + 1):
            # Single digit check: s[i-1]
            one_digit = int(s[i-1])
            if 1 <= one_digit <= 9:
                dp[i] += dp[i-1]
            
            # Two digit check: s[i-2:i]
            two_digits = int(s[i-2:i])
            if 10 <= two_digits <= 26:
                dp[i] += dp[i-2]
                
        return dp[n]
        