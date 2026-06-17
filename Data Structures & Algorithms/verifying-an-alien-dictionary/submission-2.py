class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        letter_rank = dict()
        for i in range(len(order)):
            letter_rank[order[i]] = i
        
        is_sorted = True
        
        i = 0
        j = 1
        while j < len(words):
            break_loop = False
            word1 = words[i]
            word2 = words[j]
            for k in range(min(len(word1), len(word2))):
                if letter_rank[word1[k]] > letter_rank[word2[k]]:
                    is_sorted = False
                    break_loop = True
                    break
                elif letter_rank[word1[k]] < letter_rank[word2[k]]:
                    break_loop = True
                    break
            if not break_loop and len(words[i]) > len(words[j]):
                is_sorted = False
                break
            i += 1
            j += 1

        return is_sorted