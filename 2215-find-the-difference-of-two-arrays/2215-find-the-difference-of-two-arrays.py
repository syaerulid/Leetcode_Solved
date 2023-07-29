class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums_gabungan = [[]]
        nums_satu = []
        nums_dua = []
        nums1 = set(nums1)
        nums2 = set(nums2)
        for num1 in nums1:
            if num1 not in nums2:
                nums_satu.append(num1)
        for num2 in nums2:
            if num2 not in nums1:
                nums_dua.append(num2)
                

        nums_gabungan = nums_satu, nums_dua
        return nums_gabungan

        