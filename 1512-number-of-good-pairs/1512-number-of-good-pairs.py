class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        n = len(nums)
        output = 0
        for i in range (n):
            for j in range(i + 1, n):
                if i < j and nums[i] == nums[j]:
                    output += 1
                else:
                    output += 0
        return output
        