class Solution:
    def merge(self, nums1: [int], m: int, nums2: [int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        idx1 = m - 1 #tail of nums1
        idx2 = n - 1 #tail of nums2
        idx3 = m + n - 1 #tail of nums1 + nums2

        while idx1 >= 0 and idx2 >= 0:
            if nums1[idx1] > nums2[idx2]:
                nums1[idx3] = nums1[idx1]
                idx1 -= 1
            else:
                nums1[idx3] = nums2[idx2]
                idx2 -= 1
            idx3 -= 1
        
        if idx1 < 0: # if nums is empty or not all elements of nums2 are copied
            for i in range(idx2 + 1):
                nums1[i] = nums2[i]