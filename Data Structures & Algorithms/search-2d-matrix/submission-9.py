class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 2 binary searches
        # 1. finding the the correct row
        bottom = 0
        top = len(matrix) - 1
        mid_row = 0
        while bottom <= top:
            mid_row = (bottom + top) // 2
            if matrix[mid_row][0] <= target <= matrix[mid_row][-1]:
                break
            elif target < matrix[mid_row][0]:
                top = mid_row - 1
            else:
                bottom = mid_row + 1
        
        # 2. finding whether or not the target exists in this row
        l = 0
        r = len(matrix[mid_row]) - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[mid_row][mid] == target:
                return True
            elif matrix[mid_row][mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False