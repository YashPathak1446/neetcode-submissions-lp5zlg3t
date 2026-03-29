class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_index = 0
        nums2_index = 0

        while nums2_index < n and nums1_index < m+nums2_index:
            if nums2[nums2_index] < nums1[nums1_index]:
                nums1.insert(nums1_index, nums2[nums2_index])
                nums1_index += 1
                nums2_index += 1
                nums1.pop()
                
            else:
                nums1_index += 1

        
        # End of nums1 list
        while nums2_index < n:
            nums1.insert(nums1_index, nums2[nums2_index])
            nums1.pop()
            nums1[nums1_index] = nums2[nums2_index]
            nums2_index += 1
            nums1_index += 1