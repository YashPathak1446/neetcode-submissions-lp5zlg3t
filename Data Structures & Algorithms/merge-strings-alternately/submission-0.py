class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        min_len = min(len(word1), len(word2))
        i = 0
        merged_word = ""
        while i < min_len:
            merged_word += (word1[i] + word2[i])
            i += 1

        if min_len == len(word1):
            merged_word += word2[i:]
        else:
            merged_word += word1[i:]

        return merged_word 