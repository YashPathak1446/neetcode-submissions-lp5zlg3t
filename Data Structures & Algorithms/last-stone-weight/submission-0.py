import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = sorted(stones)

        def destroy(stones):
            temp = stones[-1] - stones[-2]
            k = len(stones)

            stones.pop()
            stones.pop()

            if temp != 0:
                for i in range(len(stones)):
                    if temp <= stones[i]:
                        stones.insert(i, temp)
                        break

                if len(stones) != k - 1:
                    stones.append(temp)

        while len(stones) > 1:
            destroy(stones)

        return stones[0] if stones else 0