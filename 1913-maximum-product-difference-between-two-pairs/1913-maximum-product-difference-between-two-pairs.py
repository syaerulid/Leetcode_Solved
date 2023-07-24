class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        self.nums = nums
        sorted_asc = sorted(nums)
        sorted_desc = sorted(nums, reverse = True)

        maxi_num = sorted_desc[0]
        second_maxi_num = sorted_desc[1]

        min_num = sorted_asc[0]
        second_min_num = sorted_asc[1]

        return (maxi_num * second_maxi_num) - (min_num * second_min_num)