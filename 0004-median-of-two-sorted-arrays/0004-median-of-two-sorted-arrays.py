class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        self.nums1 = nums1
        self.nums2 = nums2

        median_val = 0

        merge_array = []
        merge_array = nums1 + nums2
        merge_array.sort()
        
        if len(merge_array) % 2 == 0:
            median_val = (merge_array[len(merge_array) // 2 - 1] + merge_array[len(merge_array) // 2]) / 2
        else:
            median_val = merge_array[len(merge_array) // 2]

        return median_val
