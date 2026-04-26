import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        closest_points_dict = dict()

        for arr in points:
            curr_distance = math.sqrt(arr[0]**2 + arr[1]**2)
            if curr_distance not in closest_points_dict:
                closest_points_dict[curr_distance] = [arr]
            else:
                closest_points_dict[curr_distance].append(arr)

        sorted_lst = sorted(list(closest_points_dict.keys()))
        print(sorted_lst)
        
        closest_points = []
        for i in range(len(sorted_lst)):
            curr_arr = closest_points_dict[sorted_lst[i]]
            if len(curr_arr) > 1:
                for j in range(len(curr_arr)):
                    if len(closest_points) < k:
                        closest_points.append(curr_arr[j])
                    else:
                        break
            else:
                if len(closest_points) < k:
                    closest_points.append(curr_arr[0])
                else:
                    break
        return closest_points