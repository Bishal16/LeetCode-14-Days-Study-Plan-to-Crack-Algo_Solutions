class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i,val in enumerate(nums):
            if target==val or target<val:
                return i            
        return i+