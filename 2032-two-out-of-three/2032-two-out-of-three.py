class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        self.nums1 = nums1
        self.nums2 = nums2
        self.nums3 = nums3
        output = []

        for num in set(nums1 + nums2 + nums3):
            count = 0
            if num in nums1 :
                count += 1
            if num in nums2 :
                count += 1
            if num in nums3:
                count += 1
            if count >= 2:
                output.append(num)
                
        return output

