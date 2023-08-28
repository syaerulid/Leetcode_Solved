class Solution:
    def sortSentence(self, s: str) -> str:

        # make string to list
        s_split = s.split(" ")
        # new sorted list
        sorted_list = sorted(s_split, key=lambda item:int(''.join(filter(str.isdigit, item))))
        
        # make it back to string before perform regex
        temp_result = " ".join(sorted_list)

        # perform regex to remove number
        pattern = r'[0-9]'
        final_result = re.sub(pattern, '', temp_result)

        return final_result

