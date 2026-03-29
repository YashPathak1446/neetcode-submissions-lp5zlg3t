class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) - 1
        mid = (top + bottom) // 2

        while top < bottom:
            if target > matrix[mid][-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bottom = mid - 1
            else:
                break
            mid = (top + bottom) // 2
        
        # print(mid)
        
        if top > bottom:
            return False
        l = 0
        r = len(matrix[mid]) - 1
        mid_row = (l + r) // 2

        # print(matrix[mid])

        while (l <= r):
            if target < matrix[mid][mid_row]:
                r = mid_row - 1
            elif target > matrix[mid][mid_row]:
                l = mid_row + 1
            else:
                return True
            mid_row = (l + r) // 2
        return False
