class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if k == len(arr): return arr
        min_separation = max(arr)
        for i in range(len(arr)):
            min_separation = min(min_separation, abs(x - arr[i]))
        
        start_index = 0
        for i in range(len(arr)):
            if abs(x - arr[i]) == min_separation:
                start_index = i
                break

        print(start_index)
        k_freq_arr = [arr[start_index]]
        l = start_index - 1
        r = start_index + 1
        while len(k_freq_arr) != k:
            if r <= len(arr) - 1 and l >= 0:
                if abs(x - arr[r]) < abs(x - arr[l]):
                    k_freq_arr.append(arr[r])
                    r += 1
                elif abs(x - arr[r]) >= abs(x - arr[l]):
                    k_freq_arr.append(arr[l])
                    l -= 1
            else:
                if r == len(arr):
                    k_freq_arr.append(arr[l])
                    l -= 1
                else:
                    k_freq_arr.append(arr[r])
                    r += 1
        return sorted(k_freq_arr)