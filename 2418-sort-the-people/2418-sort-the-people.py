class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # zip names and heights
        name_heights = list(zip(names, heights))
        # sorting based on values x[1]
        sorted_pairs = sorted(name_heights, key=lambda x: x[1], reverse=True)

        # unzip
        sorted_name, sorted_heights = zip(*sorted_pairs)
        return sorted_name
        