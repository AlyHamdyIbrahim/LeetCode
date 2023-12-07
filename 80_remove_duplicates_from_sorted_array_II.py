class Solution:
    def removeDuplicates(self, nums: [int]) -> int:
        numsLength = len(nums)
        if numsLength == 0:
            return 0
        i = 0
        j = 1
        c = 0
        while j < numsLength:
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
                c = 0
            else:
                c += 1
                if c == 1:
                    i += 1
                    nums[i] = nums[j]
            j += 1
        return i + 1