class Solution:
    def climbStairs(self, n: int) -> int:
        if n==0:
            return 0
        dp = [0]*n
        dp[0]=1
        if n==1:
            return dp[0]
        dp[1]=2
        if n==2:
            return dp[1]
        for x in range(2,n):
            dp[x]= dp[x-1]+dp[x-2]
        return dp[n-1]
        