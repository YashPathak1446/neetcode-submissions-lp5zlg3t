class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordDict = dict()
        for word in strs:
            key = "".join(sorted(word))
            if key not in wordDict:
                wordDict[key] = [word]
            else:
                wordDict[key].append(word)
            
        output_list = []
        for value in wordDict.values():
            output_list.append(value)
        return output_list