class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_words = max(len(sentence.split()) for sentence in sentences)
        return max_words