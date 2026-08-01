class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            value = 1
        if n == 2:
            value = 2
        if n>= 3:
            cache = [0]*n
            cache[0]= 1 #step1
            cache[1] = 2 #step2
            cache[2] = 3 #step3
            value = 0
            for i in range (3,n):
                value = cache[i-2]+ cache[i-1]
                cache[i] = value
            print (cache)
            value = cache[-1]
        return value

        