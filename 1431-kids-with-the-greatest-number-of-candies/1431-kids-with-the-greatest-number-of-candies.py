class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        new_candies = []
        maximum_candies = max(candies)
        output = []

        for can in candies:
            can_extra = can + extraCandies
            new_candies.append(can_extra)

        for can in new_candies:
            output.append(can >= maximum_candies)

        return output

