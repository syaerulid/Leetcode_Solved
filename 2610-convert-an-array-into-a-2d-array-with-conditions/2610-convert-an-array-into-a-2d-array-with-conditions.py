class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        ans = []
        while len(nums) > 0:
            s = set(nums)
            ans.append(list(s))
            for each in s:
                nums.remove(each)
        return ans
