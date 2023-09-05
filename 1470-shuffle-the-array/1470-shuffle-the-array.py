class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        nums_gab = []
        nums1 = nums[:n]
        nums2 = nums[n:]

        for i, j in zip(nums1, nums2):
            nums_gab.extend([i, j])
        
        return nums_gab