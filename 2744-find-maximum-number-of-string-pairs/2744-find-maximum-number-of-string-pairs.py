class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        output = 0
        word_dict = {}
        for word in words:
            reversed_word = word[::-1]
            if reversed_word in word_dict and word_dict[reversed_word] > 0:
                output += 1
                word_dict[reversed_word] -= 1
            else:
                word_dict[word] = word_dict.get(word, 0) + 1

        return output
