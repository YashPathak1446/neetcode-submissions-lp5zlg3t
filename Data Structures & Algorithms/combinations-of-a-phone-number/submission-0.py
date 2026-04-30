class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone_dict = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        result = []

        def dfs(i, current_str):
            if i >= len(digits):
                if current_str:
                    result.append(current_str)
                return
            current_lst = phone_dict[digits[i]]
            print(current_lst)

            for j in range(len(current_lst)):
                dfs(i+1, current_str + current_lst[j])
            
        dfs(0, "")
        return result
