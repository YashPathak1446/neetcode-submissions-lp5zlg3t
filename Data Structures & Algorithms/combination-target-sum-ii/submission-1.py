class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        # [1, 2, 2, 4, 5, 6, 9]
        candidate_combination = []
        curr_candidates = [] # unique

        def dfs(i):
            if sum(curr_candidates) == target:
                if curr_candidates[:] not in candidate_combination:
                    candidate_combination.append(curr_candidates[:])
                return
            if sum(curr_candidates) > target or i >= len(candidates):
                return

            curr_candidates.append(candidates[i])
            dfs(i+1)
            curr_candidates.pop()
            
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            
            dfs(i+1)
        
        dfs(0)
        return candidate_combination