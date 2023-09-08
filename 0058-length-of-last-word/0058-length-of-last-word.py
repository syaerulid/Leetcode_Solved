class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # remove trailing and leading spaces
        s_new = s.strip()
        # create new list
        s_list = s_new.split(' ')

        # return length of last element
        return len(s_list[-1])