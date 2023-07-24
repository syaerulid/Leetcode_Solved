class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        self.nums = nums
        output = 0
        maximum_number = max(nums)
        minimum_number = min(nums)

        for num in nums:
            if num < maximum_number and num > minimum_number:
                output = num
                break
            elif num == maximum_number or num == minimum_number:
                output = -1

        return output
        
