class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)

        # base case:
        if len(weights) == days:
            return l

        min_weight_capacity = r

        while l <= r:
            count = 0
            mid_weight = (r+l) // 2
            current_weight = 0
            for i in range(len(weights)):
                if current_weight + weights[i] <= mid_weight:
                    current_weight += weights[i]
                else:
                    count += 1
                    current_weight = weights[i]

            if current_weight != 0:
                count += 1
            
            if count < days:
                r = mid_weight - 1
            elif count > days:
                l = mid_weight + 1 
            else:
                min_weight_capacity = min(min_weight_capacity, mid_weight)
                r = mid_weight - 1

        if l >= r:
            min_weight_capacity = l
        return min_weight_capacity