class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = set()
        set1 = set(nums1)
        set2 = set(nums2)

        for s1 in set1:
            for s2 in set2:
                if s1 in set2:
                    output.add(s1)
                elif s2 in set1:
                    output.add(s2)

        return list(output)