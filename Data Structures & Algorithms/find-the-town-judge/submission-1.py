class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_map = dict()
        for i in range(1, n+1):
            trust_map[i] = [0]
        
        for i in range(len(trust)):
            x = trust[i][0]
            y = trust[i][1]
            if 0 in trust_map[x]:
                trust_map[x].pop()
            trust_map[x].append(y)
        
        print(trust_map)
        potential_town_judge = -1
        for k, v in trust_map.items():
            if 0 in v:
                potential_town_judge = k
                break
        for k, v in trust_map.items():
            if potential_town_judge != k and potential_town_judge not in v:
                return -1

        return potential_town_judge