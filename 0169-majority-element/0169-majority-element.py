class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        major = n // 2

        counts = Counter(nums)

        for num, count in counts.items():
            if count > major:
                return num