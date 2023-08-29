class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        n = len(nums)
        output = 0
        
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(i + 2, n):
                    if nums[j] - nums[i] == diff and nums[k] - nums[j] == diff:
                        output += 1

        return output