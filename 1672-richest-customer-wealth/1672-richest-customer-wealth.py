class Solution:
    def __init__(self):
        self.accounts = []

    def maximumWealth(self, accounts: List[List[int]]) -> int:
        self.accounts = accounts
        max_wealth = 0

        for sublist in accounts:
            current_sum = sum(sublist)
            if current_sum > max_wealth:
                max_wealth = current_sum

        return max_wealth

        
        
        