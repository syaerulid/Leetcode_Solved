class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        output = 0
        for word in words:
            if word.startswith(pref):
                output += 1
            else:
                output += 0

        return output