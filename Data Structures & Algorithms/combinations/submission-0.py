class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        curr_subset = []
        all_combos = []

        def dfs(i):
            if i > n:
                return
            if len(curr_subset) == k:
                all_combos.append(curr_subset[:])
                return
            curr_subset.append(i+1)
            dfs(i+1)
            curr_subset.pop()
            dfs(i+1)
        
        dfs(0)
        return all_combos