class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            product_left = math.prod(nums[:i])
            product_right = math.prod(nums[i+1:])
            result.append(product_left * product_right)
        
        return result
        
        