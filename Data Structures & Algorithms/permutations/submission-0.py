class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        k = len(nums)
        permutation_lst = []
        curr_lst = []

        def dfs():
            if len(curr_lst) == k:
                permutation_lst.append(curr_lst[:])
                return
            for i in range(len(nums)):
                if nums[i] not in curr_lst:
                    curr_lst.append(nums[i])
                    dfs()
                    curr_lst.pop()
                

    
        dfs()
        return permutation_lst