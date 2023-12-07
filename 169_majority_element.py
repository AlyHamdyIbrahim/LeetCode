class Solution:
    def majorityElement(self, nums: [int]) -> int:
        appearances = dict()
        for num in nums:
            if num in appearances:
                appearances[num] += 1
            else:
                appearances[num] = 1
        
        for num in appearances:
            if appearances[num] > len(nums) / 2:
                return num

    def majorityElement2(self, nums: [int]) -> int:
        c = 0
        majority = None
        for i in range(len(nums)):
            if c == 0:
                majority = nums[i]
            if nums[i] == majority:
                c += 1
            else:
                c -= 1
        return majority