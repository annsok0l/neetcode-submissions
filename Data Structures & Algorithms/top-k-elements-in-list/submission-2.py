class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        my_counter = Counter(nums)
        output = sorted(my_counter.keys(), key=lambda x: my_counter[x], reverse=True)
        sorted_output = output
        result = sorted_output[0:k]
        return result