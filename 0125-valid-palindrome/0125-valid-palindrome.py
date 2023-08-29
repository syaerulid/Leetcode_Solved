class Solution:
    def isPalindrome(self, s: str) -> bool:
        # ubah jadi lower
        s_lower = s.lower()
        # ubah jadi list
        string_list = list(s_lower)
        left, right = 0, len(string_list) - 1

        # perulangan
        while left < right:
            if not string_list[left].isalnum():
                left += 1
            elif not string_list[right].isalnum():
                right -= 1
            else:
                string_list[left], string_list[right] = string_list[right], string_list[left]
                left += 1
                right -= 1

        modif_string = "".join(string_list)
        return modif_string  == s_lower

        