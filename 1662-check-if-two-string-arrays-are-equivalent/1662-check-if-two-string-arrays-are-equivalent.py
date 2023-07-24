class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        self.word1 = word1
        self.word2 = word2

        gabungan_kata = ''
        kata_gabungan = ''

        for word in word1:
            gabungan_kata += word

        for word in word2:
            kata_gabungan += word

        return gabungan_kata == kata_gabungan
            