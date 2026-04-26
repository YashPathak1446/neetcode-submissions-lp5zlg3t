import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        new_points = []
        for point in points:
            new_points.append([math.sqrt(point[0]**2 + point[1]**2), point[0], point[1]])
        heapq.heapify(new_points)
        count = 0
        k_closest_points = []
        while count < k:
            x, y, z = heapq.heappop(new_points)
            count += 1
            k_closest_points.append([y,z])
        return k_closest_points