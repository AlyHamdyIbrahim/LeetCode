class Solution:
    def rotate(self, nums: [int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k = k % length
        nums = nums[0:length-k][::-1] + nums[length-k:][::-1]
        nums = nums[::-1]

    def rotate2(self, nums: [int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k = k % length
        nums = nums[length-k:] + nums[:length-k]