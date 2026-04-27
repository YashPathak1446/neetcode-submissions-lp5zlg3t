class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        permutation_lst = []
        curr_perm = []
        used_indices_set = set()

        def dfs():
            if len(curr_perm) == len(nums):
                permutation_lst.append(curr_perm[:])
                return
            
            for i in range(len(nums)):
                if i in used_indices_set:
                    continue

                if i > 0 and nums[i] == nums[i-1] and (i-1) not in used_indices_set:
                    continue
                curr_perm.append(nums[i])
                used_indices_set.add(i)
                dfs()
                curr_perm.pop()
                used_indices_set.remove(i)
            
        dfs()
        return permutation_lst