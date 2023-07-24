from typing import List

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_words = 0  # Initialize the max_words to 0

        for sen in sentences:
            words = sen.split(' ')
            num_words = len(words)

            if num_words > max_words:
                max_words = num_words

        return max_words
