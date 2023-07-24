class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        self.items = items
        self.ruleKey = ruleKey
        self.ruleValue = ruleValue

        total_result = 0
        for item in items:
            if ruleKey == "type" and ruleValue == item[0]:
                total_result += 1
            elif ruleKey == "color" and ruleValue == item[1]:
                total_result += 1
            elif ruleKey == "name" and ruleValue == item[2]:
                total_result += 1
        
        return total_result