class Solution:
    def maxArea(self, heights: List[int]) -> int:
        best_result = 0
        i = 0
        j = len(heights)-1
        while i<j:
            result = (j-i)*min(heights[i], heights[j])
            if result> best_result:
                best_result = result
            if heights[i]<heights[j]:
                i+=1
            else:
                j-=1
        return best_result

            
            
                


        