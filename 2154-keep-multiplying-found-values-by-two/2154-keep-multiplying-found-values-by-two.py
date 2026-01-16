class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:            
        found = set(nums)  
        while original in found:
            original *= 2
        return original


        