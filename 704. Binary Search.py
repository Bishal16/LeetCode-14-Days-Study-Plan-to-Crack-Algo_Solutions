class Solution:
    def search(self, nums: List[int], target: int) -> int:
        end = len(nums)-1
        start = 0
        while(start<= end):
            mid = (start+end)//2
            if nums[mid] == target:
                return mid
            elif target >= nums[start] and target <= nums[mid]:
                end = mid
            elif target > nums[mid] and target <= nums[end]:
                start = mid+1                
            else :
                return -1
        