class Solution:
    def removeDuplicates(self, nums: [int]) -> int:
        numsLength = len(nums)
        if numsLength == 0:
            return 0
        i = 0
        j = 1
        while j < numsLength:
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
                j += 1
            else:
                j += 1
        return i + 1
    