class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        # create empty list for reversed list and list_mix
        reversed_list = []
        list_mix = []
        # create conditions when number after reversed is 0, the reverse become number itself
        for num in nums:
            reversed_num = int(str(num)[::-1]) 
            if reversed_num == 0:
                reversed_list.append(num)
            else:
                reversed_list.append(reversed_num)

        # concat the original list and reversed list
        list_mix = nums + reversed_list
        # make a set to count unique
        set_mix = set(list_mix)
        # return length of unique elements (nunique)
        return len(set_mix)