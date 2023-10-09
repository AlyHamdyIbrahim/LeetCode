class Solution:
    def searchInsert(self, nums: [int], target: int) -> int:
        r = len(nums) - 1
        l = 0

        while l <= r:
            
            mid = l + (r - l) // 2

            if nums[mid] == target:
                return mid
            
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return mid + 1 if nums[mid] < target else mid

print(Solution().searchInsert([1,3,5,6], 4))
