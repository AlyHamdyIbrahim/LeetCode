class Solution:
    def removeElement(self, nums: [int], val: int) -> int:
        numsLength = len(nums)
        if numsLength == 0:
            return 0
        i = -1
        j = 0
        while j < numsLength:
            if nums[j] == val:
                j += 1
            else:
                i += 1
                nums[i] = nums[j]
                j += 1
        return i + 1
