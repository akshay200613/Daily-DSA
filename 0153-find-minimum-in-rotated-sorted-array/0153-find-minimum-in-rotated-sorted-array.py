class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        
        while low < high:
            mid = low + (high - low) // 2
            
            if nums[mid] > nums[high]:
                # Minimum is in the right half
                low = mid + 1
            else:
                # Minimum is in the left half (including mid)
                high = mid
        
        return nums[low]
        