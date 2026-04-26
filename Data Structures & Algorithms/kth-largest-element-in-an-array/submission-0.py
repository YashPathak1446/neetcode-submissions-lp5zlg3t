import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] = -nums[i]
        heapq.heapify(nums)
        count = 0
        k_largest_element = 0
        while count < k:
            k_largest_element = heapq.heappop(nums)
            count += 1
        return -k_largest_element
