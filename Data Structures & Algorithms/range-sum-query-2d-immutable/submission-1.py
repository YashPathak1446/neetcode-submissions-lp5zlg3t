class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total_sum = 0
        curr_row = row1
        curr_col = col1
        for l in range(row1, row2 + 1):
            for w in range(col1, col2 + 1):
                total_sum += self.matrix[l][w]
        
        return total_sum



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)