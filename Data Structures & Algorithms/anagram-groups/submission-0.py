class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output_list = [[strs[0]]]

        for word in strs[1:]:
            added_prev = False
            for j in range(len(output_list)):
                if sorted(word) == sorted(output_list[j][0]):
                    output_list[j].append(word)
                    added_prev = True
            if added_prev == False:
                output_list.append([word])
        
        return output_list
                    

        return output_list
