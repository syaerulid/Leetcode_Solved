class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        ans = []
        while len(nums) > 0:
            s = set(nums)  # Create a set of unique values from nums
            ans.append(list(s))  # Append the list of unique values to ans
            for each in s:
                nums.remove(each)  # Remove each unique value from nums
        return ans