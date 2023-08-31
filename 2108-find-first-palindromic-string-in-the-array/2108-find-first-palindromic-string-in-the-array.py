from collections import deque
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        queue = deque(words)
        # buat deque kosong
        pal = deque() 
        for word in queue:
            if word == word[::-1]:
                pal.appendleft(word)

        hasil = []
        for p in pal:
            hasil.append(p)

        reversed_hasil = hasil[::-1]
        if reversed_hasil:
            join_hasil = "".join(reversed_hasil[0])
            return join_hasil
        else:
            return ""
        