class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        new_grid = []
        output = 0
        for sublist in grid:
            for sub in sublist:
                new_grid.append(sub)
        neg_number = []
        for new in new_grid:
            if new < 0:
                neg_number.append(new)

        return len(neg_number)
