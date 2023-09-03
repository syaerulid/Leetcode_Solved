class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        num = arrivalTime + delayedTime
        if num == 24:
            return 0
        elif num > 24:
            return num - 24
        else:
            return num
            
        