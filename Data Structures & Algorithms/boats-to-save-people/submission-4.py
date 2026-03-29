class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        min_boats = 0
        l = 0
        r = len(people) - 1
        people.sort()
        while l < r:
            if people[l] + people[r] <= limit:
                min_boats += 1
                l += 1
                r -= 1
            elif people[r] == limit:
                min_boats += 1
                r -= 1
            elif people[l] + people[r] > limit:
                min_boats += 1
                r -= 1
        if l == r:
            min_boats += 1
        return min_boats