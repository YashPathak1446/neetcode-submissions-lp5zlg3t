class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len_str = len(min(strs))
        curr_letter = ""
        longest_common_prefix = ""
        for i in range(min_len_str):
            curr_letter = strs[0][i]
            for word in strs:
                if word[i] != curr_letter:
                    return longest_common_prefix
            longest_common_prefix += curr_letter

        return longest_common_prefix