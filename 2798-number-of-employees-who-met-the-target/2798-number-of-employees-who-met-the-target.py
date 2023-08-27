class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        output = 0
        for emp in hours:
            if emp >= target:
                output += 1
            else:
                output += 0

        return output