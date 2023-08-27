class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        output = ''
        for word in words:
            output += word[0]
        return output == s