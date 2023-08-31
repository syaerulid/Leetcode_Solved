class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        output = 0

        for pat in patterns:
            if pat in word:
                output += 1
            else:
                output += 0

        return output