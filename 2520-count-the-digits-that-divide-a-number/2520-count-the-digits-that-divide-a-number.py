class Solution:
    def countDigits(self, num: int) -> int:
        output = 0
        # change num to str
        str_num = str(num)

        # create a list
        num_list = list(map(int, str_num))
        for n in num_list:
            if num % n == 0:
                output += 1
            else:
                output += 0
        return output