class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = dict()

        def recurse(curr_string):
            if curr_string in memo:
                return memo[curr_string]
                
            if len(curr_string) == 0:
                return True
            
            for word in wordDict:
                if curr_string[0:len(word)] == word:
                    answer = recurse(curr_string[len(word):])
                    memo[curr_string] = answer
                    if answer == True:
                        return answer
            memo[curr_string] = False
            return False

        answer = recurse(s)
        return answer