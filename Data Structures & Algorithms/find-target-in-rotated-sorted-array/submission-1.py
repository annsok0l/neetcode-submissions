class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1

        while low<high:
            mid = low + (high-low)//2
            
            if nums[mid]>nums[high]:
                low = mid+1 
                              
            else:
                high = mid
                    
        pivot = low
        if target >= nums[pivot] and target <= nums[-1]:
            our_list = nums[pivot:]
            offset = pivot
        else:
            our_list = nums[:pivot]
            offset = 0
            
        low = 0
        high = len(our_list)-1
        while low<=high:
            mid = low + (high-low)//2
            
            if our_list[mid]== target:
                return mid + offset
            elif our_list[mid]>target:
                high = mid-1
            elif our_list[mid]<target:
                low = mid+1
        return -1