class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        self.sentence = sentence
        
        alphabet = list(string.ascii_lowercase)
        set_alpha = set(alphabet)
        set_sentence = set(sentence)
                
        if len(set_alpha) == len(set_sentence):
            return True
        else:
            return False
        
        