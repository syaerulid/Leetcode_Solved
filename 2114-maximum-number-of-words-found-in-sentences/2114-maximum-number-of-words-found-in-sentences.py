class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        self.sentences = sentences
        
        max_words = max(len(sen.split()) for sen in sentences)
        return max_words