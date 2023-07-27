class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos_list = []
        neg_list = []
        max_output = 0
        for num in nums:
            if num > 0:
                pos_list.append(num)
            elif num < 0:
                neg_list.append(num)

        len_pos = len(pos_list)
        len_neg = len(neg_list)

        if len_pos > len_neg:
            max_output = len_pos
        else:
            max_output = len_neg

        return max_output