class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        numbers = sorted(nums)
        print(numbers)
        for i in range(len(numbers)):
            a = numbers[i]
            if a > 0:
                break

            if i > 0 and a == numbers[i - 1]:
                continue
            l = i+1
            r = len(numbers)-1
            while l<r:
                threeSum = numbers[i] + numbers[l]+numbers[r]
                if threeSum>0:
                    r-=1
                elif threeSum<0:
                    l+=1
                else:
                    triplet = [numbers[i], numbers[l], numbers[r]]
                    results.append(triplet)
                    l+=1
                    r-=1
                    while numbers[l] == numbers[l - 1] and l < r:
                        l += 1

        return results