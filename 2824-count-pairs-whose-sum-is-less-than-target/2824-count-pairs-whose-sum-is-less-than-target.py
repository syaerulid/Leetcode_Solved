class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        output = 0
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n): # membuktikan j > i
                if i >= 0 and i < j :
                    if nums[i] + nums[j] < target:
                        output += 1
                    else:
                        output += 0
            
        return output
        
    
    
        